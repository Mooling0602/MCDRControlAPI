"""Default event listeners for MCDReforged to call.
"""
from mcdreforged.api.all import \
    PluginServerInterface, CommandSource
from mcdreforged.api.command import CommandContext
from mcdreforged.api.command import SimpleCommandBuilder
from mcdreforged.api.command import Boolean
from mcdr_control_api import app

import mcdr_control_api


builder = SimpleCommandBuilder()
fastapi_mcdr = None  # pylint: disable=invalid-name
"""Shared instance of the fastapi_mcdr plugin.
"""


def on_load(server: PluginServerInterface, prev_module):  # pylint: disable=unused-argument
    """Called when the plugin is loaded.
    """
    global fastapi_mcdr  # pylint: disable=global-statement
    mcdr_control_api.psi = server
    mcdr_control_api.app_id = server.get_self_metadata().id
    server.logger.info("on_load")
    builder.arg('use_logger', Boolean)
    builder.register(server)
    fastapi_mcdr = server.get_plugin_instance('fastapi_mcdr')
    if fastapi_mcdr is not None and fastapi_mcdr.is_ready():
        server.logger.info("on_load.start")
        mount_app()
    server.register_event_listener(
        fastapi_mcdr.COLLECT_EVENT,  # type: ignore
        mount_app
    )


def on_unload(server: PluginServerInterface):  # pylint: disable=unused-argument
    """Called when the plugin is unloaded.
    """
    if fastapi_mcdr:
        if mcdr_control_api.app_id:
            fastapi_mcdr.unmount(mcdr_control_api.app_id)


def mount_app():
    """Called when the app will be mounted by fastapi_mcdr.
    """
    if fastapi_mcdr:
        fastapi_mcdr.mount(mcdr_control_api.app_id, app)

@builder.command('!!ctl_api print <use_logger>')
def on_command_node_print(src: CommandSource, ctx: CommandContext):  # pylint: disable=unused-argument
    """Debug command to print something need test.

    Usage: `!!ctl_api print <use_logger>`
    """
    server = mcdr_control_api.psi
    if not isinstance(server, PluginServerInterface):
        return
    result = str(server.get_self_metadata().version)
    if ctx['use_logger']:
        server.logger.info(result)
    else:
        print(result)

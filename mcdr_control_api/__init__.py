"""mcdr_control_api

A simple API for controlling mcdreforged server.
"""
from enum import StrEnum, auto
from fastapi import FastAPI, Query
from mcdreforged.api.types import PluginServerInterface
from mcdreforged.constants.core_constant import VERSION as mcdr_ver


app = FastAPI()
app_id: str | None = None
psi: PluginServerInterface | None = None


class Path(StrEnum):
    """The target you may want to query for.
    """
    PLUGIN = auto()
    MCDR = auto()


@app.get("/test")
async def test():
    """A test endpoint to check if this FastAPI instance(app) is working fine.

    If so, it will return a string `"Hello, MCDReforged!"`.
    """
    return "Hello, MCDReforged!"


@app.get("/app_id")
async def get_app_id():
    """Return the app_id of this FastAPI instance.

    If app works fine, it will return a string of its `app_id`.
    """
    if app_id:
        return app_id
    else:
        return {"error": "app not inited!"}


@app.get("/query/{path}/{search_key}")
async def query(
    path: Path,
    search_key: str,
    other: str | None = Query(default=None)
):
    """Query for the information of the MCDReforged server.

    
    """
    if not isinstance(psi, PluginServerInterface):
        raise RuntimeError("MCDR plugin server interface not initialized!")
    match path:
        case Path.PLUGIN:
            match search_key:
                case "ver" | "version":
                    if other is None:
                        return str(
                            psi.get_self_metadata().version)
        case Path.MCDR:
            match search_key:
                case "ver" | "version":
                    if other is None:
                        return str(mcdr_ver)
                case "status":
                    if other is None:
                        return {
                            "version": str(mcdr_ver),
                            "is_running": True,
                            "is_server_running": psi.is_server_running(),
                            "is_server_startup": psi.is_server_startup(),
                            "is_rcon_running": psi.is_rcon_running(),
                            "plugin_count": len(psi.get_plugin_list()),
                            "server_pid": psi.get_server_pid(),
                            "server_version": psi.get_server_information().version
                        }
                    else:
                        match other:
                            case "ver" | "version":
                                return str(mcdr_ver)
                            case "is_running":
                                return True
                            case "is_server_running":
                                return psi.is_server_running()
                            case  "is_server_startup":
                                return psi.is_server_startup()
                            case  "is_rcon_running":
                                return psi.is_rcon_running()
                            case "plugin_count":
                                return len(psi.get_plugin_list())
                            case "server_pid":
                                return psi.get_server_pid()
                            case "server_version":
                                return psi.get_server_information().version

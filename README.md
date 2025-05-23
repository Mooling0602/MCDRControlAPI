# MCDRControlAPI
A simple API for controlling MCDReforged server.

## Usage
1. Install FastAPIMCDR from MCDR console: `!!MCDR plg install fastapi_mcdr [--confirm]`
> If you want to install without running MCDR server, open the plugin folder and run `mcdreforged pim download fastapi_mcdr && mcdreforged pim pipi FastAPI*.mcdr`

2. Configure FastAPIMCDR, edit the host(address) and the port.

3. Install this plugin from release.
> Once this plugin committed to [PluginCatalogue](https://github.com/MCDReforged/PluginCatalogue), you can install it from MCDR console: `!!MCDR plg install mcdr_control_api [--confirm]`

4. Now you can see the API document at `http://<host>:<port>/mcdr_control_api/docs`
> You can also configure HTTPS, then use `https://<domain>[/<path>]/mcdr_control_api/docs`

## NOTICE
- At present all informations this plugin provides are opened to public, so if you don't want to expose some your server information, you can configure in the config file.
> Config part is developing, so no release for this plugin. You shouldn't use this plugin in your production environment!

- APIs for controlling MCDR server is still developing...
from ncclient import manager
import env
import xml.dom.minidom

print('Connecting...')
with manager.connect(
    host=env.IOS_XE_1["host"],
    port=env.IOS_XE_1["netconf_port"],
    username=env.IOS_XE_1["username"],
    password=env.IOS_XE_1["password"],
    hostkey_verify=False
) as m:
    netconf_reply = m.get_config(source='running')
    with open('2_devices_output.txt', 'w') as f:
        print('Writing server config to file...')
        f.write(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

print('Done.')

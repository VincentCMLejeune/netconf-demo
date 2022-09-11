from ncclient import manager, xml_
import env
import xml.dom.minidom

save_body = """
<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
"""

print("Connecting...")
with manager.connect(
        host=env.IOS_XE_1["host"],
        port=env.IOS_XE_1["netconf_port"],
        username=env.IOS_XE_1["username"],
        password=env.IOS_XE_1["password"],
        hostkey_verify=False
) as m:
    print("Sending a RPC operation to the device...")
    netconf_reply = m.dispatch(xml_.to_ele(save_body))
    with open('4_save_config_output.txt', 'w') as f:
        print('Writing raw XML data returned from the device...')
        f.write(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

print("Done.")

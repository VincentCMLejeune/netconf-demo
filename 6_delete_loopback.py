from ncclient import manager
import xml.dom.minidom
import env

netconf_interface_template = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="delete">
        	<name>{name}</name>
        </interface>
    </interfaces>
</config>"""

new_loopback_name = "Loopback" + input("What loopback number to delete ? ")
netconf_data = netconf_interface_template.format(
    name=new_loopback_name
)


print("Opening NETCONF Connection...")
with manager.connect(
        host=env.IOS_XE_1["host"],
        port=env.IOS_XE_1["netconf_port"],
        username=env.IOS_XE_1["username"],
        password=env.IOS_XE_1["password"],
        hostkey_verify=False
) as m:
    print("Sending a <edit-config> operation to the device.\n")
    netconf_reply = m.edit_config(netconf_data, target='running')

with open('6_delete_loopback_output.txt', 'w') as f:
    print('Writing raw XML data returned from the device...')
    f.write(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

print("Done.")

from ncclient import manager
import xml.dom.minidom

import env

netconf_data = """
            <config>
              <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                  <name>Loopback110</name>
                  <description>Pod Number 10</description>
                  <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                    ianaift:softwareLoopback
                  </type>
                  <enabled>true</enabled>
                  <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                      <ip>10.111.10.2</ip>
                      <netmask>255.255.255.255</netmask>
                    </address>
                  </ipv4>
                </interface>
              </interfaces>
            </config>"""

print("Opening NETCONF Connection...")
with manager.connect(
        host=env.IOS_XE_1["host"],
        port=env.IOS_XE_1["netconf_port"],
        username=env.IOS_XE_1["username"],
        password=env.IOS_XE_1["password"],
        hostkey_verify=False
) as m:
    print("Sending a <edit-config> operation to the device...")
    netconf_reply = m.edit_config(netconf_data, target='running')

with open('5_add_loopback_output.txt', 'w') as f:
    print('Writing raw XML data returned from the device...')
    f.write(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

print("Done.")

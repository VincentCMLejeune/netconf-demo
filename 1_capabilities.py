from ncclient import manager
import env

print('Connecting...')
m = manager.connect(
    host=env.IOS_XE_1["host"],
    port=env.IOS_XE_1["netconf_port"],
    username=env.IOS_XE_1["username"],
    password=env.IOS_XE_1["password"],
    hostkey_verify=False
)

with open('1_capabilities_output.txt', 'w') as f:
    print('Writing server capabilities to file...')
    for capability in m.server_capabilities:
        f.write(capability)
        f.write('\n')

print('Done.')

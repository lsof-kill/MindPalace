import pandas
import csv
import ast

df = pandas.read_csv('last_year_data.csv')
hdr_data = {}
fields=['Host', 'User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding', 'Content-Type', 'Content-Length', 'Origin', 'Connection', 'Referer', 'Upgrade-Insecure-Requests', 'Cache-Control', 'Accept-Charset', 'x-datadog-trace-id', 'x-datadog-parent-id', 'x-datadog-sampling-priority', 'Range', 'User-agent', 'X-Loop-Control', 'user-agent', 'host', 'User_Agent', 'Proxy-Connection', 'Pragma', 'Cache-control', 'Cookie', 'TE', 'AcceptAccept-Encoding', 'Keep-Alive', 'Authorization', 'BS_REAL_IP', 'X-Chrome-Variations', 'X-Password', 'Proxy-Authorization', 'Client-IP', 'X-Forwarded-For', 'NSC_USER', 'NSC_NONCE', 'accept', 'Useragent', 'SOAPAction', 'Content-type', 'Client-DPAP-Version', 'Via', 'DNT', 'X-Forwarded-Proto', 'X-Real-IP', 'X-Requested-With', 'Depth', 'Access-Control-Request-Method', 'content-length', 'content-type', 'accept-encoding', 'referer', 'accept-language', 'X-Proxy-ID', 'HOST', 'Connection-Type', 'Sec-Gpc', 'If-Modified-Since', 'X-BlueCoat-Via', 'X-STATUS', 'connection', 'accept-charset', 'Orgin', 'x-radius-11', 'x-imsi', 'x-imei', 'x-up-vfza-id', 'Client-ATV-Sharing-Version', 'Client-DAAP-Version', 'Client-iTunes-Sharing-Version', 'Viewer-Only-Client', 'Expect', 'COntent-Length']
for key in fields:
    hdr_data[key] = []

for hdr in df['headers']:
    current_attr=[]
    # print("============header=============")
    try:
        for attr in ast.literal_eval(hdr[hdr.find("["):hdr.rfind("]")+1]):
            if(type(attr)!=str):
                type_attr = attr[0]
                val_attr = attr[1]
            else:
                type_attr = attr.split(": ",1)[0]
                val_attr = attr.split(": ",1)[1]
            current_attr.append(type_attr)

            if type_attr in hdr_data:
                hdr_data[type_attr].append(val_attr)
            else:
                hdr_data[type_attr] = [val_attr]
                # input()


        for i in hdr_data:
            if i not in current_attr:
                hdr[i].append('')
            # print(hdr_data)
            # input()
    except:
        for key in hdr_data:
            hdr_data[key].append('')




print("=========done=========")
# pandas.DataFrame.from_dict(hdr_data)
ans = pandas.DataFrame.from_dict(hdr_data,orient='index').T
print(type(ans))
print(ans.head(10))
ans.to_csv("headerFull.csv", index=False)



import xml.etree.ElementTree as ET
import sys

tree = ET.parse(sys.argv[1])
root = tree.getroot()
report=root.find('Report')
print "Host\tPort\tVersion\tCipher\tKx\tAu\tEnc\tKeylen\tMac\tExport"
for host in report.findall('ReportHost'):
        for item in host.findall('ReportItem'):
                hname = host.attrib['name']
                if item.attrib['pluginID'] == "21643":
                        pname = item.attrib['port']
                        out = item.find('plugin_output')
                        currentver = ''
                        for line in out.text.split('\n'):
                                if line.startswith("    "):
                                        if line.startswith("      ")==False:
                                                currentver = line.strip()
                                        else:
                                                splitted = line.split(' ')
                                                cipher = ''
                                                kx = ''
                                                au = ''
                                                enc = ''
                                                keylen = ''
                                                mac = ''
                                                export = 0
                                                for cipherattrib in splitted:
                                                        if cipherattrib.startswith("Kx="):
                                                                kx = cipherattrib.strip()[3:]
                                                        if cipherattrib.startswith("Au="):
                                                                au = cipherattrib.strip()[3:]
                                                        if cipherattrib.startswith("Enc="):
                                                                enc = cipherattrib.strip()[4:]
                                                                keylen = enc[enc.find('(')+1:enc.find(')')]
                                                                enc = enc[:enc.find('(')]
                                                        if cipherattrib.startswith("Mac="):
                                                                mac = cipherattrib.strip()[4:]
                                                        if "export" in cipherattrib:
                                                                export = 1
                                                cipher = splitted[6]    
                                                print hname+'\t'+pname+'\t'+currentver+'\t'+cipher+'\t'+kx+'\t'+au+'\t'+enc+'\t'+keylen+'\t'+mac+'\t'+str(export)

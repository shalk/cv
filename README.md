
##NAME
    cv -  cloudview  configure tools

##Usage: 

    cv -h|-help|--help
    cv <Command>  <Option>

##Example:

    cv setup vcell
    cv setup cvm
    cv delete cvm

    cv print vcell
    cv print cvm

##Command:

    setup   : setup cvm and vcell
    delete  : delete cvm
    print   : print cvm or vcell configure file

    zk      : configure zkclient.xml
    ntp     : configure crontab for time sync
    host    : configure mq_prop.properties and agent_prop.properties
    network : configure vlan-conf and nic-conf
    service : check service status( host-agent,devagentd ,storage-agent,zkclient,collet-agent,ntp)

    storage : 
    
    usage   : display usage
    version : display version


##COPYRIGHT

    Copyright (C) 2014  Shalk
    
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



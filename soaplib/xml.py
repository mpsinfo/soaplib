#
# soaplib - Copyright (C) 2009 Aaron Bickell, Jamie Kirkpatrick
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#

from soaplib.etimport import ElementTree


class NamespaceLookup(object):
    '''
    Class to manage XML namespaces
    '''

    def __init__(self, tns = None, wsdl_map = False):
        self.nsmap = {
            'xs': 'http://www.w3.org/2001/XMLSchema',
            'xsi': 'http://www.w3.org/1999/XMLSchema-instance',
        }
        if wsdl_map:
            self.nsmap['soap'] = 'http://schemas.xmlsoap.org/wsdl/soap/'
            self.nsmap['wsdl'] = 'http://schemas.xmlsoap.org/wsdl/'
        else:
            self.nsmap['SOAP-ENC'] \
                = 'http://schemas.xmlsoap.org/soap/encoding/'
            self.nsmap['SOAP-ENV'] \
                = 'http://schemas.xmlsoap.org/soap/envelope/'
        if tns is not None:
            self.nsmap['tns'] = tns
            self.nsmap['typens'] = tns

    def get_all(self):
        '''
        Return all namespaces
        '''
        return self.nsmap

    def get(self, key):
        '''
        Lookup and return a given namespace
        '''
        if key in self.nsmap:
            ns = self.nsmap[key]
        else:
            ns = ''
        return "{%s}" % ns

    def set(self, key, ns):
        '''
        Add a namespace to the map (replaces)
        '''
        self.nsmap[key] = ns

'''
Default namespace lookup
'''
ns = NamespaceLookup()


def qualify(name, ns):
    '''
    Qualify an idenifier with a namespace
    '''
    return "{%s}%s" % (ns, name)


def create_xml_element(name, nslookup, default_ns=None):
    '''
    Factory method to create a new XML element
    @param default_ns The default namespace to use for the element.
    @param extended_map A mapping of any additional namespaces to add.
    '''
    if default_ns is not None:
        namespace_map = {None: default_ns}
    else:
        namespace_map = {}
    for key, value in nslookup.get_all().iteritems():
        if value != default_ns:
            namespace_map[key] = value
    return ElementTree.Element(name, nsmap=namespace_map)


def create_xml_subelement(parent, name):
    '''
    Factory method to create a new XML subelement
    '''
    if not name.startswith("{") and None in parent.nsmap:
        name = qualify(name, parent.nsmap[None])
    return ElementTree.SubElement(parent, name)

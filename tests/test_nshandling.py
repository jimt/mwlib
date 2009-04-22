#! /usr/bin/env py.test

from mwlib import nshandling, siteinfo
siteinfo_de = siteinfo.get_siteinfo("de")
assert siteinfo_de, "cannot find german siteinfo"

def test_fqname():
    def get_fqname(name, expected):
        fqname = nsmapper.get_fqname(name)
        print "%r -> %r" % (name, fqname)
        assert fqname==expected
        
    nsmapper = nshandling.nsmapper(siteinfo_de)

    d = get_fqname
    e = "Benutzer:Schmir"
    
    yield d, "User:Schmir", e
    yield d, "user:Schmir", e
    yield d, "benutzer:schmir", e
    yield d, " user: schmir ", e
    yield d, "___user___:___schmir  __", e
    
def test_fqname_defaultns():
    def get_fqname(name, expected):
        fqname = nsmapper.get_fqname(name, 10) # Vorlage
        print "%r -> %r" % (name, fqname)
        assert fqname==expected
    
    nsmapper = nshandling.nsmapper(siteinfo_de)
    d = get_fqname

    yield d, "user:schmir", "Benutzer:Schmir"
    yield d, "schmir", "Vorlage:Schmir"
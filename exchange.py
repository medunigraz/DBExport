# ./exchange.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e62bbb3832d0d2d8af859293d6d1d84c17031970
# Generated 2016-07-04 11:38:23.140406 by PyXB version 1.2.4 using Python 3.5.2.final.0
# Namespace https://online.medunigraz.at/webservice-STPL.xsd

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0cd84590-41cb-11e6-bc99-705a0f5f5f4b')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('https://online.medunigraz.at/webservice-STPL.xsd', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {https://online.medunigraz.at/webservice-STPL.xsd}EXCHANGEType with content type ELEMENT_ONLY
class EXCHANGEType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {https://online.medunigraz.at/webservice-STPL.xsd}EXCHANGEType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'EXCHANGEType')
    _XSDLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {https://online.medunigraz.at/webservice-STPL.xsd}STPL uses Python identifier STPL
    __STPL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'STPL'), 'STPL', '__httpsonline_medunigraz_atwebservice_STPL_xsd_EXCHANGEType_httpsonline_medunigraz_atwebservice_STPL_xsdSTPL', True, pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 6, 6), )

    
    STPL = property(__STPL.value, __STPL.set, None, None)

    
    # Element {https://online.medunigraz.at/webservice-STPL.xsd}LV uses Python identifier LV
    __LV = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LV'), 'LV', '__httpsonline_medunigraz_atwebservice_STPL_xsd_EXCHANGEType_httpsonline_medunigraz_atwebservice_STPL_xsdLV', True, pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 7, 6), )

    
    LV = property(__LV.value, __LV.set, None, None)

    
    # Element {https://online.medunigraz.at/webservice-STPL.xsd}PV uses Python identifier PV
    __PV = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PV'), 'PV', '__httpsonline_medunigraz_atwebservice_STPL_xsd_EXCHANGEType_httpsonline_medunigraz_atwebservice_STPL_xsdPV', True, pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 8, 6), )

    
    PV = property(__PV.value, __PV.set, None, None)

    _ElementMap.update({
        __STPL.name() : __STPL,
        __LV.name() : __LV,
        __PV.name() : __PV
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'EXCHANGEType', EXCHANGEType)


# Complex type {https://online.medunigraz.at/webservice-STPL.xsd}PVType with content type EMPTY
class PVType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {https://online.medunigraz.at/webservice-STPL.xsd}PVType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PVType')
    _XSDLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 11, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute NR uses Python identifier NR
    __NR = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NR'), 'NR', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_NR', pyxb.binding.datatypes.int)
    __NR._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 12, 4)
    __NR._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 12, 4)
    
    NR = property(__NR.value, __NR.set, None, None)

    
    # Attribute LV_NR uses Python identifier LV_NR
    __LV_NR = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'LV_NR'), 'LV_NR', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_LV_NR', pyxb.binding.datatypes.int, required=True)
    __LV_NR._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 13, 4)
    __LV_NR._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 13, 4)
    
    LV_NR = property(__LV_NR.value, __LV_NR.set, None, None)

    
    # Attribute DATUM_DER_LETZTBEURTEILUNG uses Python identifier DATUM_DER_LETZTBEURTEILUNG
    __DATUM_DER_LETZTBEURTEILUNG = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DATUM_DER_LETZTBEURTEILUNG'), 'DATUM_DER_LETZTBEURTEILUNG', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_DATUM_DER_LETZTBEURTEILUNG', pyxb.binding.datatypes.dateTime)
    __DATUM_DER_LETZTBEURTEILUNG._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 14, 4)
    __DATUM_DER_LETZTBEURTEILUNG._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 14, 4)
    
    DATUM_DER_LETZTBEURTEILUNG = property(__DATUM_DER_LETZTBEURTEILUNG.value, __DATUM_DER_LETZTBEURTEILUNG.set, None, None)

    
    # Attribute NOTE uses Python identifier NOTE
    __NOTE = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NOTE'), 'NOTE', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_NOTE', pyxb.binding.datatypes.string)
    __NOTE._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 15, 4)
    __NOTE._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 15, 4)
    
    NOTE = property(__NOTE.value, __NOTE.set, None, None)

    
    # Attribute PRF_VERSUCH uses Python identifier PRF_VERSUCH
    __PRF_VERSUCH = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PRF_VERSUCH'), 'PRF_VERSUCH', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_PRF_VERSUCH', pyxb.binding.datatypes.int)
    __PRF_VERSUCH._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 16, 4)
    __PRF_VERSUCH._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 16, 4)
    
    PRF_VERSUCH = property(__PRF_VERSUCH.value, __PRF_VERSUCH.set, None, None)

    
    # Attribute TITEL uses Python identifier TITEL
    __TITEL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TITEL'), 'TITEL', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_TITEL', pyxb.binding.datatypes.string)
    __TITEL._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 17, 4)
    __TITEL._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 17, 4)
    
    TITEL = property(__TITEL.value, __TITEL.set, None, None)

    
    # Attribute PRUEFER_VORNAME uses Python identifier PRUEFER_VORNAME
    __PRUEFER_VORNAME = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PRUEFER_VORNAME'), 'PRUEFER_VORNAME', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_PRUEFER_VORNAME', pyxb.binding.datatypes.string)
    __PRUEFER_VORNAME._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 18, 4)
    __PRUEFER_VORNAME._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 18, 4)
    
    PRUEFER_VORNAME = property(__PRUEFER_VORNAME.value, __PRUEFER_VORNAME.set, None, None)

    
    # Attribute PRUEFER_NACHNAME uses Python identifier PRUEFER_NACHNAME
    __PRUEFER_NACHNAME = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PRUEFER_NACHNAME'), 'PRUEFER_NACHNAME', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_PRUEFER_NACHNAME', pyxb.binding.datatypes.string)
    __PRUEFER_NACHNAME._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 19, 4)
    __PRUEFER_NACHNAME._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 19, 4)
    
    PRUEFER_NACHNAME = property(__PRUEFER_NACHNAME.value, __PRUEFER_NACHNAME.set, None, None)

    
    # Attribute GESCHLECHT uses Python identifier GESCHLECHT
    __GESCHLECHT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GESCHLECHT'), 'GESCHLECHT', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_GESCHLECHT', pyxb.binding.datatypes.string)
    __GESCHLECHT._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 20, 4)
    __GESCHLECHT._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 20, 4)
    
    GESCHLECHT = property(__GESCHLECHT.value, __GESCHLECHT.set, None, None)

    
    # Attribute MATRIKELNUMMER uses Python identifier MATRIKELNUMMER
    __MATRIKELNUMMER = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'MATRIKELNUMMER'), 'MATRIKELNUMMER', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_MATRIKELNUMMER', pyxb.binding.datatypes.int)
    __MATRIKELNUMMER._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 21, 4)
    __MATRIKELNUMMER._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 21, 4)
    
    MATRIKELNUMMER = property(__MATRIKELNUMMER.value, __MATRIKELNUMMER.set, None, None)

    
    # Attribute SKZ uses Python identifier SKZ
    __SKZ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SKZ'), 'SKZ', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_SKZ', pyxb.binding.datatypes.string)
    __SKZ._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 22, 4)
    __SKZ._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 22, 4)
    
    SKZ = property(__SKZ.value, __SKZ.set, None, None)

    
    # Attribute STUDIENPLANVERSION uses Python identifier STUDIENPLANVERSION
    __STUDIENPLANVERSION = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'STUDIENPLANVERSION'), 'STUDIENPLANVERSION', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_STUDIENPLANVERSION', pyxb.binding.datatypes.string)
    __STUDIENPLANVERSION._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 23, 4)
    __STUDIENPLANVERSION._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 23, 4)
    
    STUDIENPLANVERSION = property(__STUDIENPLANVERSION.value, __STUDIENPLANVERSION.set, None, None)

    
    # Attribute ANERKENNUNG_JA_NEIN uses Python identifier ANERKENNUNG_JA_NEIN
    __ANERKENNUNG_JA_NEIN = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ANERKENNUNG_JA_NEIN'), 'ANERKENNUNG_JA_NEIN', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_ANERKENNUNG_JA_NEIN', pyxb.binding.datatypes.string)
    __ANERKENNUNG_JA_NEIN._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 24, 4)
    __ANERKENNUNG_JA_NEIN._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 24, 4)
    
    ANERKENNUNG_JA_NEIN = property(__ANERKENNUNG_JA_NEIN.value, __ANERKENNUNG_JA_NEIN.set, None, None)

    
    # Attribute ANERKENNUNGSTITEL_DT uses Python identifier ANERKENNUNGSTITEL_DT
    __ANERKENNUNGSTITEL_DT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ANERKENNUNGSTITEL_DT'), 'ANERKENNUNGSTITEL_DT', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_ANERKENNUNGSTITEL_DT', pyxb.binding.datatypes.string)
    __ANERKENNUNGSTITEL_DT._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 25, 4)
    __ANERKENNUNGSTITEL_DT._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 25, 4)
    
    ANERKENNUNGSTITEL_DT = property(__ANERKENNUNGSTITEL_DT.value, __ANERKENNUNGSTITEL_DT.set, None, None)

    
    # Attribute ANERKENNUNGSTITEL_ENGL uses Python identifier ANERKENNUNGSTITEL_ENGL
    __ANERKENNUNGSTITEL_ENGL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ANERKENNUNGSTITEL_ENGL'), 'ANERKENNUNGSTITEL_ENGL', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_ANERKENNUNGSTITEL_ENGL', pyxb.binding.datatypes.string)
    __ANERKENNUNGSTITEL_ENGL._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 26, 4)
    __ANERKENNUNGSTITEL_ENGL._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 26, 4)
    
    ANERKENNUNGSTITEL_ENGL = property(__ANERKENNUNGSTITEL_ENGL.value, __ANERKENNUNGSTITEL_ENGL.set, None, None)

    
    # Attribute ANERKENNUNGS_ECTS uses Python identifier ANERKENNUNGS_ECTS
    __ANERKENNUNGS_ECTS = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ANERKENNUNGS_ECTS'), 'ANERKENNUNGS_ECTS', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_ANERKENNUNGS_ECTS', pyxb.binding.datatypes.int)
    __ANERKENNUNGS_ECTS._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 27, 4)
    __ANERKENNUNGS_ECTS._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 27, 4)
    
    ANERKENNUNGS_ECTS = property(__ANERKENNUNGS_ECTS.value, __ANERKENNUNGS_ECTS.set, None, None)

    
    # Attribute ANERKENNUNGS_GHK uses Python identifier ANERKENNUNGS_GHK
    __ANERKENNUNGS_GHK = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ANERKENNUNGS_GHK'), 'ANERKENNUNGS_GHK', '__httpsonline_medunigraz_atwebservice_STPL_xsd_PVType_ANERKENNUNGS_GHK', pyxb.binding.datatypes.int)
    __ANERKENNUNGS_GHK._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 28, 4)
    __ANERKENNUNGS_GHK._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 28, 4)
    
    ANERKENNUNGS_GHK = property(__ANERKENNUNGS_GHK.value, __ANERKENNUNGS_GHK.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __NR.name() : __NR,
        __LV_NR.name() : __LV_NR,
        __DATUM_DER_LETZTBEURTEILUNG.name() : __DATUM_DER_LETZTBEURTEILUNG,
        __NOTE.name() : __NOTE,
        __PRF_VERSUCH.name() : __PRF_VERSUCH,
        __TITEL.name() : __TITEL,
        __PRUEFER_VORNAME.name() : __PRUEFER_VORNAME,
        __PRUEFER_NACHNAME.name() : __PRUEFER_NACHNAME,
        __GESCHLECHT.name() : __GESCHLECHT,
        __MATRIKELNUMMER.name() : __MATRIKELNUMMER,
        __SKZ.name() : __SKZ,
        __STUDIENPLANVERSION.name() : __STUDIENPLANVERSION,
        __ANERKENNUNG_JA_NEIN.name() : __ANERKENNUNG_JA_NEIN,
        __ANERKENNUNGSTITEL_DT.name() : __ANERKENNUNGSTITEL_DT,
        __ANERKENNUNGSTITEL_ENGL.name() : __ANERKENNUNGSTITEL_ENGL,
        __ANERKENNUNGS_ECTS.name() : __ANERKENNUNGS_ECTS,
        __ANERKENNUNGS_GHK.name() : __ANERKENNUNGS_GHK
    })
Namespace.addCategoryObject('typeBinding', 'PVType', PVType)


# Complex type {https://online.medunigraz.at/webservice-STPL.xsd}LVType with content type EMPTY
class LVType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {https://online.medunigraz.at/webservice-STPL.xsd}LVType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LVType')
    _XSDLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 30, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute NR uses Python identifier NR
    __NR = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NR'), 'NR', '__httpsonline_medunigraz_atwebservice_STPL_xsd_LVType_NR', pyxb.binding.datatypes.int, required=True)
    __NR._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 31, 4)
    __NR._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 31, 4)
    
    NR = property(__NR.value, __NR.set, None, None)

    
    # Attribute GHK uses Python identifier GHK
    __GHK = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GHK'), 'GHK', '__httpsonline_medunigraz_atwebservice_STPL_xsd_LVType_GHK', pyxb.binding.datatypes.int, required=True)
    __GHK._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 32, 4)
    __GHK._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 32, 4)
    
    GHK = property(__GHK.value, __GHK.set, None, None)

    
    # Attribute LVNR uses Python identifier LVNR
    __LVNR = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'LVNR'), 'LVNR', '__httpsonline_medunigraz_atwebservice_STPL_xsd_LVType_LVNR', pyxb.binding.datatypes.string)
    __LVNR._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 33, 4)
    __LVNR._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 33, 4)
    
    LVNR = property(__LVNR.value, __LVNR.set, None, None)

    
    # Attribute STOFFSEMESTER uses Python identifier STOFFSEMESTER
    __STOFFSEMESTER = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'STOFFSEMESTER'), 'STOFFSEMESTER', '__httpsonline_medunigraz_atwebservice_STPL_xsd_LVType_STOFFSEMESTER', pyxb.binding.datatypes.string)
    __STOFFSEMESTER._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 34, 4)
    __STOFFSEMESTER._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 34, 4)
    
    STOFFSEMESTER = property(__STOFFSEMESTER.value, __STOFFSEMESTER.set, None, None)

    
    # Attribute TITEL uses Python identifier TITEL
    __TITEL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TITEL'), 'TITEL', '__httpsonline_medunigraz_atwebservice_STPL_xsd_LVType_TITEL', pyxb.binding.datatypes.string)
    __TITEL._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 35, 4)
    __TITEL._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 35, 4)
    
    TITEL = property(__TITEL.value, __TITEL.set, None, None)

    
    # Attribute UNTERTITEL uses Python identifier UNTERTITEL
    __UNTERTITEL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UNTERTITEL'), 'UNTERTITEL', '__httpsonline_medunigraz_atwebservice_STPL_xsd_LVType_UNTERTITEL', pyxb.binding.datatypes.string)
    __UNTERTITEL._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 36, 4)
    __UNTERTITEL._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 36, 4)
    
    UNTERTITEL = property(__UNTERTITEL.value, __UNTERTITEL.set, None, None)

    
    # Attribute TITEL_ENGL uses Python identifier TITEL_ENGL
    __TITEL_ENGL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TITEL_ENGL'), 'TITEL_ENGL', '__httpsonline_medunigraz_atwebservice_STPL_xsd_LVType_TITEL_ENGL', pyxb.binding.datatypes.string)
    __TITEL_ENGL._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 37, 4)
    __TITEL_ENGL._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 37, 4)
    
    TITEL_ENGL = property(__TITEL_ENGL.value, __TITEL_ENGL.set, None, None)

    
    # Attribute UNTERTITEL_ENG uses Python identifier UNTERTITEL_ENG
    __UNTERTITEL_ENG = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UNTERTITEL_ENG'), 'UNTERTITEL_ENG', '__httpsonline_medunigraz_atwebservice_STPL_xsd_LVType_UNTERTITEL_ENG', pyxb.binding.datatypes.string)
    __UNTERTITEL_ENG._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 38, 4)
    __UNTERTITEL_ENG._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 38, 4)
    
    UNTERTITEL_ENG = property(__UNTERTITEL_ENG.value, __UNTERTITEL_ENG.set, None, None)

    
    # Attribute LV_ART uses Python identifier LV_ART
    __LV_ART = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'LV_ART'), 'LV_ART', '__httpsonline_medunigraz_atwebservice_STPL_xsd_LVType_LV_ART', pyxb.binding.datatypes.string)
    __LV_ART._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 39, 4)
    __LV_ART._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 39, 4)
    
    LV_ART = property(__LV_ART.value, __LV_ART.set, None, None)

    
    # Attribute SWS uses Python identifier SWS
    __SWS = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SWS'), 'SWS', '__httpsonline_medunigraz_atwebservice_STPL_xsd_LVType_SWS', pyxb.binding.datatypes.int)
    __SWS._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 40, 4)
    __SWS._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 40, 4)
    
    SWS = property(__SWS.value, __SWS.set, None, None)

    
    # Attribute CREDITS uses Python identifier CREDITS
    __CREDITS = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CREDITS'), 'CREDITS', '__httpsonline_medunigraz_atwebservice_STPL_xsd_LVType_CREDITS', pyxb.binding.datatypes.decimal)
    __CREDITS._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 41, 4)
    __CREDITS._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 41, 4)
    
    CREDITS = property(__CREDITS.value, __CREDITS.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __NR.name() : __NR,
        __GHK.name() : __GHK,
        __LVNR.name() : __LVNR,
        __STOFFSEMESTER.name() : __STOFFSEMESTER,
        __TITEL.name() : __TITEL,
        __UNTERTITEL.name() : __UNTERTITEL,
        __TITEL_ENGL.name() : __TITEL_ENGL,
        __UNTERTITEL_ENG.name() : __UNTERTITEL_ENG,
        __LV_ART.name() : __LV_ART,
        __SWS.name() : __SWS,
        __CREDITS.name() : __CREDITS
    })
Namespace.addCategoryObject('typeBinding', 'LVType', LVType)


# Complex type {https://online.medunigraz.at/webservice-STPL.xsd}STPLType with content type ELEMENT_ONLY
class STPLType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {https://online.medunigraz.at/webservice-STPL.xsd}STPLType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'STPLType')
    _XSDLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 43, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {https://online.medunigraz.at/webservice-STPL.xsd}FACH uses Python identifier FACH
    __FACH = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FACH'), 'FACH', '__httpsonline_medunigraz_atwebservice_STPL_xsd_STPLType_httpsonline_medunigraz_atwebservice_STPL_xsdFACH', True, pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 45, 6), )

    
    FACH = property(__FACH.value, __FACH.set, None, None)

    
    # Attribute SKZ_UNI uses Python identifier SKZ_UNI
    __SKZ_UNI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SKZ_UNI'), 'SKZ_UNI', '__httpsonline_medunigraz_atwebservice_STPL_xsd_STPLType_SKZ_UNI', pyxb.binding.datatypes.string)
    __SKZ_UNI._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 47, 4)
    __SKZ_UNI._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 47, 4)
    
    SKZ_UNI = property(__SKZ_UNI.value, __SKZ_UNI.set, None, None)

    
    # Attribute SKZ_KEY uses Python identifier SKZ_KEY
    __SKZ_KEY = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SKZ_KEY'), 'SKZ_KEY', '__httpsonline_medunigraz_atwebservice_STPL_xsd_STPLType_SKZ_KEY', pyxb.binding.datatypes.string)
    __SKZ_KEY._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 48, 4)
    __SKZ_KEY._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 48, 4)
    
    SKZ_KEY = property(__SKZ_KEY.value, __SKZ_KEY.set, None, None)

    
    # Attribute SKZKEY uses Python identifier SKZKEY
    __SKZKEY = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SKZKEY'), 'SKZKEY', '__httpsonline_medunigraz_atwebservice_STPL_xsd_STPLType_SKZKEY', pyxb.binding.datatypes.int)
    __SKZKEY._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 49, 4)
    __SKZKEY._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 49, 4)
    
    SKZKEY = property(__SKZKEY.value, __SKZKEY.set, None, None)

    
    # Attribute SKZBEZ uses Python identifier SKZBEZ
    __SKZBEZ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SKZBEZ'), 'SKZBEZ', '__httpsonline_medunigraz_atwebservice_STPL_xsd_STPLType_SKZBEZ', pyxb.binding.datatypes.string)
    __SKZBEZ._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 50, 4)
    __SKZBEZ._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 50, 4)
    
    SKZBEZ = property(__SKZBEZ.value, __SKZBEZ.set, None, None)

    
    # Attribute VERSION uses Python identifier VERSION
    __VERSION = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'VERSION'), 'VERSION', '__httpsonline_medunigraz_atwebservice_STPL_xsd_STPLType_VERSION', pyxb.binding.datatypes.string)
    __VERSION._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 51, 4)
    __VERSION._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 51, 4)
    
    VERSION = property(__VERSION.value, __VERSION.set, None, None)

    
    # Attribute GUELTIG_AB uses Python identifier GUELTIG_AB
    __GUELTIG_AB = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GUELTIG_AB'), 'GUELTIG_AB', '__httpsonline_medunigraz_atwebservice_STPL_xsd_STPLType_GUELTIG_AB', pyxb.binding.datatypes.dateTime)
    __GUELTIG_AB._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 52, 4)
    __GUELTIG_AB._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 52, 4)
    
    GUELTIG_AB = property(__GUELTIG_AB.value, __GUELTIG_AB.set, None, None)

    
    # Attribute GUELTIG_BIS uses Python identifier GUELTIG_BIS
    __GUELTIG_BIS = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'GUELTIG_BIS'), 'GUELTIG_BIS', '__httpsonline_medunigraz_atwebservice_STPL_xsd_STPLType_GUELTIG_BIS', pyxb.binding.datatypes.string)
    __GUELTIG_BIS._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 53, 4)
    __GUELTIG_BIS._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 53, 4)
    
    GUELTIG_BIS = property(__GUELTIG_BIS.value, __GUELTIG_BIS.set, None, None)

    
    # Attribute STUDIERBAR_BIS uses Python identifier STUDIERBAR_BIS
    __STUDIERBAR_BIS = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'STUDIERBAR_BIS'), 'STUDIERBAR_BIS', '__httpsonline_medunigraz_atwebservice_STPL_xsd_STPLType_STUDIERBAR_BIS', pyxb.binding.datatypes.string)
    __STUDIERBAR_BIS._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 54, 4)
    __STUDIERBAR_BIS._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 54, 4)
    
    STUDIERBAR_BIS = property(__STUDIERBAR_BIS.value, __STUDIERBAR_BIS.set, None, None)

    
    # Attribute ABSCHNITT uses Python identifier ABSCHNITT
    __ABSCHNITT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ABSCHNITT'), 'ABSCHNITT', '__httpsonline_medunigraz_atwebservice_STPL_xsd_STPLType_ABSCHNITT', pyxb.binding.datatypes.int)
    __ABSCHNITT._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 55, 4)
    __ABSCHNITT._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 55, 4)
    
    ABSCHNITT = property(__ABSCHNITT.value, __ABSCHNITT.set, None, None)

    
    # Attribute SEMESTER uses Python identifier SEMESTER
    __SEMESTER = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SEMESTER'), 'SEMESTER', '__httpsonline_medunigraz_atwebservice_STPL_xsd_STPLType_SEMESTER', pyxb.binding.datatypes.int)
    __SEMESTER._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 56, 4)
    __SEMESTER._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 56, 4)
    
    SEMESTER = property(__SEMESTER.value, __SEMESTER.set, None, None)

    
    # Attribute SWS uses Python identifier SWS
    __SWS = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SWS'), 'SWS', '__httpsonline_medunigraz_atwebservice_STPL_xsd_STPLType_SWS', pyxb.binding.datatypes.int)
    __SWS._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 57, 4)
    __SWS._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 57, 4)
    
    SWS = property(__SWS.value, __SWS.set, None, None)

    
    # Attribute CREDITS uses Python identifier CREDITS
    __CREDITS = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CREDITS'), 'CREDITS', '__httpsonline_medunigraz_atwebservice_STPL_xsd_STPLType_CREDITS', pyxb.binding.datatypes.decimal)
    __CREDITS._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 58, 4)
    __CREDITS._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 58, 4)
    
    CREDITS = property(__CREDITS.value, __CREDITS.set, None, None)

    _ElementMap.update({
        __FACH.name() : __FACH
    })
    _AttributeMap.update({
        __SKZ_UNI.name() : __SKZ_UNI,
        __SKZ_KEY.name() : __SKZ_KEY,
        __SKZKEY.name() : __SKZKEY,
        __SKZBEZ.name() : __SKZBEZ,
        __VERSION.name() : __VERSION,
        __GUELTIG_AB.name() : __GUELTIG_AB,
        __GUELTIG_BIS.name() : __GUELTIG_BIS,
        __STUDIERBAR_BIS.name() : __STUDIERBAR_BIS,
        __ABSCHNITT.name() : __ABSCHNITT,
        __SEMESTER.name() : __SEMESTER,
        __SWS.name() : __SWS,
        __CREDITS.name() : __CREDITS
    })
Namespace.addCategoryObject('typeBinding', 'STPLType', STPLType)


# Complex type {https://online.medunigraz.at/webservice-STPL.xsd}FACHType with content type ELEMENT_ONLY
class FACHType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {https://online.medunigraz.at/webservice-STPL.xsd}FACHType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FACHType')
    _XSDLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 60, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {https://online.medunigraz.at/webservice-STPL.xsd}GHK uses Python identifier GHK
    __GHK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GHK'), 'GHK', '__httpsonline_medunigraz_atwebservice_STPL_xsd_FACHType_httpsonline_medunigraz_atwebservice_STPL_xsdGHK', True, pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 62, 6), )

    
    GHK = property(__GHK.value, __GHK.set, None, None)

    
    # Attribute CREDITS uses Python identifier CREDITS
    __CREDITS = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CREDITS'), 'CREDITS', '__httpsonline_medunigraz_atwebservice_STPL_xsd_FACHType_CREDITS', pyxb.binding.datatypes.decimal)
    __CREDITS._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 64, 4)
    __CREDITS._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 64, 4)
    
    CREDITS = property(__CREDITS.value, __CREDITS.set, None, None)

    
    # Attribute SWS uses Python identifier SWS
    __SWS = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SWS'), 'SWS', '__httpsonline_medunigraz_atwebservice_STPL_xsd_FACHType_SWS', pyxb.binding.datatypes.int)
    __SWS._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 65, 4)
    __SWS._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 65, 4)
    
    SWS = property(__SWS.value, __SWS.set, None, None)

    
    # Attribute KENNUNG uses Python identifier KENNUNG
    __KENNUNG = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'KENNUNG'), 'KENNUNG', '__httpsonline_medunigraz_atwebservice_STPL_xsd_FACHType_KENNUNG', pyxb.binding.datatypes.string)
    __KENNUNG._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 66, 4)
    __KENNUNG._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 66, 4)
    
    KENNUNG = property(__KENNUNG.value, __KENNUNG.set, None, None)

    
    # Attribute NAME uses Python identifier NAME
    __NAME = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NAME'), 'NAME', '__httpsonline_medunigraz_atwebservice_STPL_xsd_FACHType_NAME', pyxb.binding.datatypes.string)
    __NAME._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 67, 4)
    __NAME._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 67, 4)
    
    NAME = property(__NAME.value, __NAME.set, None, None)

    
    # Attribute NAME_ENGL uses Python identifier NAME_ENGL
    __NAME_ENGL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NAME_ENGL'), 'NAME_ENGL', '__httpsonline_medunigraz_atwebservice_STPL_xsd_FACHType_NAME_ENGL', pyxb.binding.datatypes.string)
    __NAME_ENGL._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 68, 4)
    __NAME_ENGL._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 68, 4)
    
    NAME_ENGL = property(__NAME_ENGL.value, __NAME_ENGL.set, None, None)

    _ElementMap.update({
        __GHK.name() : __GHK
    })
    _AttributeMap.update({
        __CREDITS.name() : __CREDITS,
        __SWS.name() : __SWS,
        __KENNUNG.name() : __KENNUNG,
        __NAME.name() : __NAME,
        __NAME_ENGL.name() : __NAME_ENGL
    })
Namespace.addCategoryObject('typeBinding', 'FACHType', FACHType)


# Complex type {https://online.medunigraz.at/webservice-STPL.xsd}GHKType with content type EMPTY
class GHKType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {https://online.medunigraz.at/webservice-STPL.xsd}GHKType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GHKType')
    _XSDLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 70, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute TITEL uses Python identifier TITEL
    __TITEL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TITEL'), 'TITEL', '__httpsonline_medunigraz_atwebservice_STPL_xsd_GHKType_TITEL', pyxb.binding.datatypes.string, required=True)
    __TITEL._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 71, 4)
    __TITEL._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 71, 4)
    
    TITEL = property(__TITEL.value, __TITEL.set, None, None)

    
    # Attribute KURZBEZEICHNUNG uses Python identifier KURZBEZEICHNUNG
    __KURZBEZEICHNUNG = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'KURZBEZEICHNUNG'), 'KURZBEZEICHNUNG', '__httpsonline_medunigraz_atwebservice_STPL_xsd_GHKType_KURZBEZEICHNUNG', pyxb.binding.datatypes.string, required=True)
    __KURZBEZEICHNUNG._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 72, 4)
    __KURZBEZEICHNUNG._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 72, 4)
    
    KURZBEZEICHNUNG = property(__KURZBEZEICHNUNG.value, __KURZBEZEICHNUNG.set, None, None)

    
    # Attribute CREDITS uses Python identifier CREDITS
    __CREDITS = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CREDITS'), 'CREDITS', '__httpsonline_medunigraz_atwebservice_STPL_xsd_GHKType_CREDITS', pyxb.binding.datatypes.decimal)
    __CREDITS._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 73, 4)
    __CREDITS._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 73, 4)
    
    CREDITS = property(__CREDITS.value, __CREDITS.set, None, None)

    
    # Attribute STP_LV_NR uses Python identifier STP_LV_NR
    __STP_LV_NR = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'STP_LV_NR'), 'STP_LV_NR', '__httpsonline_medunigraz_atwebservice_STPL_xsd_GHKType_STP_LV_NR', pyxb.binding.datatypes.int, required=True)
    __STP_LV_NR._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 74, 4)
    __STP_LV_NR._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 74, 4)
    
    STP_LV_NR = property(__STP_LV_NR.value, __STP_LV_NR.set, None, None)

    
    # Attribute NR uses Python identifier NR
    __NR = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NR'), 'NR', '__httpsonline_medunigraz_atwebservice_STPL_xsd_GHKType_NR', pyxb.binding.datatypes.int)
    __NR._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 75, 4)
    __NR._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 75, 4)
    
    NR = property(__NR.value, __NR.set, None, None)

    
    # Attribute SWS uses Python identifier SWS
    __SWS = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'SWS'), 'SWS', '__httpsonline_medunigraz_atwebservice_STPL_xsd_GHKType_SWS', pyxb.binding.datatypes.int)
    __SWS._DeclarationLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 76, 4)
    __SWS._UseLocation = pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 76, 4)
    
    SWS = property(__SWS.value, __SWS.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __TITEL.name() : __TITEL,
        __KURZBEZEICHNUNG.name() : __KURZBEZEICHNUNG,
        __CREDITS.name() : __CREDITS,
        __STP_LV_NR.name() : __STP_LV_NR,
        __NR.name() : __NR,
        __SWS.name() : __SWS
    })
Namespace.addCategoryObject('typeBinding', 'GHKType', GHKType)


EXCHANGE = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EXCHANGE'), EXCHANGEType, location=pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', EXCHANGE.name().localName(), EXCHANGE)



EXCHANGEType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'STPL'), STPLType, scope=EXCHANGEType, location=pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 6, 6)))

EXCHANGEType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LV'), LVType, scope=EXCHANGEType, location=pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 7, 6)))

EXCHANGEType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PV'), PVType, scope=EXCHANGEType, location=pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 8, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 6, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 7, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 8, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EXCHANGEType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'STPL')), pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 6, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(EXCHANGEType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LV')), pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 7, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(EXCHANGEType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PV')), pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 8, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
EXCHANGEType._Automaton = _BuildAutomaton()




STPLType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FACH'), FACHType, scope=STPLType, location=pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 45, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(STPLType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FACH')), pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 45, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
STPLType._Automaton = _BuildAutomaton_()




FACHType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GHK'), GHKType, scope=FACHType, location=pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 62, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 62, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FACHType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GHK')), pyxb.utils.utility.Location('/home/users/FladischerMichael/Development/MUG/DBExport/exchange.xsd', 62, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FACHType._Automaton = _BuildAutomaton_2()


class Taxon(object):
    def __init__(self, id=None,taxonID=None,acceptedNameUsageID=None,
                 parentNameUsageID=None,nameAccordingToID=None,
                 scientificName=None,order=None,family=None,genus=None,
                 subgenus=None,specificEpithet=None,infraspecificEpithet=None,
                  taxonRank=None,scientificNameAuthorship=None,
                  taxonomicStatus=None,modified=None,license=None,
                  bibliographicCitation=None,references=None):
        self.id=id
        self.taxonID=surname
        self.acceptedNameUsageID=age
        self.parentNameUsageID=country
        self.nameAccordingToID=nameAccordingToID
        self.scientificName=scientificName
        self.order=order
        self.family=family
        self.genus=genus
        self.subgenus=subgenus
        self.specificEpithet=specificEpithet
        self.infraspecificEpithet=infraspecificEpithet
        self.taxonRank=taxonRank
        self.scientificNameAuthorship=scientificNameAuthorship
        self.taxonomicStatus=taxonomicStatus
        self.modified=modified
        self.license=license
        self.bibliographicCitation=bibliographicCitation
        self.references=references

class Province(object):
    def __init__(self, pr_id=None,abbreviation=None,name=None,designation=None):
        self.pr_id=pr_id
        self.abbreviation=abbreviation
        self.name=name
        self.designation=designation

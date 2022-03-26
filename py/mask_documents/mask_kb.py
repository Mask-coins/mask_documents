import os

from rdflib import Graph, URIRef
from rdflib.query import Result

DIR_mo = "../../ontology"
DIR_mc = "../../category"
DIR_mr = "../../resource"
PREFIX = {
    "mo": "https://github.com/Mask-coins/mask_documents/ontology/",
    "mc": "https://github.com/Mask-coins/mask_documents/category/",
    "mr": "https://github.com/Mask-coins/mask_documents/resource/",
}


def _check():
    g = Graph()
    for d in [DIR_mo, DIR_mc, DIR_mr]:
        for filename in os.listdir(d):
            if filename.endswith(".ttl"):
                file_path = os.path.join(d, filename)
                g.parse(file_path, format='turtle')
                print(file_path)
    ret :Result = g.query("SELECT DISTINCT * WHERE { ?s ?p ?o . } LIMIT 1000")
    print(len(ret))
    st = set()
    for s,p,o in ret:
        st.add(s)


class TripleLoader(object):
    _Graph = Graph()
    _Done = {}
    _ClassTree = dict()
    _RegionTree = dict()

    @classmethod
    def _load(cls,directory):
        if directory not in cls._Done:
            cls._Done[directory] = False
        if not cls._Done[directory]:
            for filename in os.listdir(directory):
                if filename.endswith(".ttl"):
                    file_path = os.path.join(directory, filename)
                    cls._Graph.parse(file_path, format='turtle')

    @classmethod
    def load_ontology(cls):
        cls._load(DIR_mo)

    @classmethod
    def load_category(cls):
        cls._load(DIR_mc)

    @classmethod
    def load_resource(cls):
        cls._load(DIR_mr)

    @classmethod
    def load_ken_all(cls):
        cls._load(DIR_mr+"/ken_all")

    @classmethod
    def get_graph(cls):
        return cls._Graph

    @classmethod
    def _category_tree_call(cls, c:URIRef, depth: int):
        print("  "*depth + str(c).replace(PREFIX["mc"], ""))
        if c in cls._ClassTree:
            for chi in cls._ClassTree[c]:
                cls._category_tree_call(chi, depth + 1)

    @classmethod
    def show_category_tree(cls, head="Root"):
        cls.load_category()
        p = URIRef(PREFIX["mo"]+"SubCategory")
        ret: Result = cls._Graph.triples((None,p,None))
        for s,p,o in ret:
            if s not in cls._ClassTree:
                cls._ClassTree[s] = []
            cls._ClassTree[s].append(o)
        node_head = URIRef(PREFIX["mc"]+head)
        cls._category_tree_call(node_head, 0)

    @classmethod
    def _region_tree_call(cls, c:URIRef, depth: int):
        print("  "*depth + str(c).replace(PREFIX["mr"], ""))
        if c in cls._RegionTree:
            for chi in cls._RegionTree[c]:
                cls._region_tree_call(chi, depth + 1)

    @classmethod
    def show_region_tree(cls, head="中四国地方"):
        cls.load_resource()
        p = URIRef(PREFIX["mo"]+"SubRegion")
        ret: Result = cls._Graph.triples((None,p,None))
        for s,p,o in ret:
            if s not in cls._RegionTree:
                cls._RegionTree[s] = []
            cls._RegionTree[s].append(o)
        node_head = URIRef(PREFIX["mr"]+head)
        cls._region_tree_call(node_head, 0)



if __name__ == "__main__":
    t = TripleLoader()
    # t.show_category_tree()
    t.show_region_tree()

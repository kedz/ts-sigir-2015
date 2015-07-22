import re
import os


def make_invisible(layers, xml):
    for layer in layers:
        print layer
        m = re.search(r'(<g[^>]+?id="' + layer + r'"[^>]+>)', xml, 
            re.DOTALL)
        layer_tag = m.groups()[0]
        layer_tag_inv = layer_tag.replace("display:inline", "display:none")
        xml = xml.replace(layer_tag, layer_tag_inv)
    return xml        

def make_visible(layers, xml):
    for layer in layers:
        m = re.search(r'(<g[^>]+?id="' + layer + r'"[^>]+>)', xml, 
            re.DOTALL)
        layer_tag = m.groups()[0]
        layer_tag_vis = layer_tag.replace("display:none", "display:inline")
        print layer_tag_vis
        xml = xml.replace(layer_tag, layer_tag_vis)
    return xml        


def main():
    with open("clustering.svg", "r") as f:
        xml = f.read()

    layers = ["unbiased_assignments", "biased_assignments",
              "unbiased_clusters", "ex_label", "label", 
              "salient_regions"]
    img_layers = [["label", ],
        ["label",  "unbiased_assignments",],
        ["label", "points", "unbiased_assignments", "ex_label"],
        ["label", "points", "unbiased_assignments", "ex_label", 
            "unbiased_clusters"],
        ["label", "points"],
        ["label", "points", "salient_regions",],
        ["label", "points", "salient_regions", "biased_assignments"],]

    for i, img_layer in enumerate(img_layers, 1):
        print i, img_layer
        xml = make_invisible(layers, xml)    
        xml = make_visible(img_layer, xml) 
        
        fname = "cluster_anim{}.svg".format(i)
        dest = "cluster_anim{}.pdf".format(i)
        with open(fname, "w") as f:
            f.write(xml)
        os.system("inkscape -z -C -f {} -A {}".format(fname, dest))
        os.remove(fname)

if __name__ == "__main__":
    main()

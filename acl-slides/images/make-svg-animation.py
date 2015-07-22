import re
import os


def make_invisible(layers, xml):
    for layer in layers:
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
    with open("stream-images.svg", "r") as f:
        xml = f.read()

    layers = ["clock", "hour1art1", "hour1art2", "hour1art3", "hour1art4", 
        "hour1blur", "hour1updates", "hour2bg", "hour2", "hour2art1", 
        "hour2art2", "hour2art3", "hour2art4", "hour2blur", "hour2updates"]

    clock_layers = ["15_minutes", "quarterhour", "30_minutes", "halfhour",
        "45_minutes", "three_quarter", "1hour", "four_quarter", "zero_minutes",
        "2hour"]
    img_layers = [layers[:1] + ["zero_minutes"],
        layers[:2] + ["15_minutes", "quarterhour"],
        layers[:3] + ["30_minutes", "halfhour"],
        layers[:4] + ["45_minutes", "three_quarter"],
        layers[:5] + ["zero_minutes", "1hour", "four_quarter"],
        layers[:6] + ["zero_minutes", "1hour", "four_quarter"],
        layers[:7] + ["zero_minutes", "1hour", "four_quarter"],
        #layers[7:8] + ["zero_minutes", "1hour", "clock"],
        ["zero_minutes", "1hour", "clock"],
        [layers[9]] + ["1hour", "15_minutes", "quarterhour", "clock"],
        layers[9:11] + ["1hour", "30_minutes", "halfhour", "clock"],
        layers[9:12] + ["1hour", "45_minutes", "three_quarter", "clock"],
        layers[9:13] + ["2hour", "zero_minutes", "four_quarter", "clock"],
        layers[9:14] + ["2hour", "zero_minutes", "four_quarter", "clock"],
        layers[9:15] + ["2hour", "zero_minutes", "four_quarter", "clock"]]
            
            #layers[:3], layers[:4], layers[:5],
            #layers[:6], layers[:7], layers[:8], layers[:9], layers[:10],
            #layers[:11], layers[:12], layers[:13], layers[:14], layers[:15]]

    for i, img_layer in enumerate(img_layers, 1):
        print i, img_layer
        xml = make_invisible(layers + clock_layers, xml)    
        xml = make_visible(img_layer, xml) 
        
        fname = "anim{}.svg".format(i)
        dest = "anim{}.pdf".format(i)
        with open(fname, "w") as f:
            f.write(xml)
        os.system("inkscape -z -C -f {} -A {}".format(fname, dest))
        os.remove(fname)

if __name__ == "__main__":
    main()

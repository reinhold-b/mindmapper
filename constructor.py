from configurations import Configs, Metrics


class MapConstructor:

    @staticmethod
    def construct(structure):
        title = list(structure.keys())[0]
        main_nodes_dict, lines_pos = Metrics.MAP_GEOMETRY(structure)
        with open(f"{title}.html", "w+") as new_file:
            new_file.write(HTML.top(title))
        with open(f"{title}.html", "a") as file:
            file.write(HTML.title_node(title))
            for i in range(0, len(list(main_nodes_dict.keys()))):
                file.write(HTML.node(list(main_nodes_dict.keys())[
                           i], list(main_nodes_dict.values())[i]))
            for i in range(0, len(lines_pos)):
                file.write(HTML.line(lines_pos[i]))
            file.write(HTML.bottom())
        with open("add.css", "w+") as new_css:
            new_css.write(CSS.css())


class HTML:

    @staticmethod
    def top(title: str) -> str:
        return f"""
<!DOCTYPE HTML>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="add.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@900&family=Roboto+Mono:ital,wght@0,400;1,300&display=swap" rel="stylesheet">
</head>
<body>
<div id="corpus">"""

    @staticmethod
    def title_node(title: str) -> str:
        return f"""
<div class="node" id="title" title="{title}">
    <p>{title}</p>
</div>"""

    @staticmethod
    def node(content, pos) -> str:
        return f"""
<div class="node" title="{content}" style="left:{pos[0]}px; top: {pos[1]}px;">
    <p>{content}</p>
</div>"""

    @staticmethod
    def line(pos):
        """
        return a HTML Marku with according parameters
        """
        return f"""
<div class="line" style="left:{pos[0][0]}px;top:{pos[0][1]}px;transform:rotate({pos[2]}deg);width:calc({pos[1]}px + 15px);"></div>"""

    @staticmethod
    def bottom() -> str:
        return """
</div>
</body>
</html> """


# CSS ------------------

class CSS:

    @staticmethod
    def css():
        left, top = Metrics.POS_TITLE_NODE()
        node_width, node_height = Metrics.node_size()
        return f"""
.node {{
    z-index: 10;
    background-color:  #5E4AE3;
    position: absolute;
    border-radius: 15px;
    width: {node_width}px;
    height: {node_height}px;
    text-align: center;
}}

#title {{
    top: {top}px;
    left: {left}px;
    font-size: 1.3rem;
    background-color:  #F46036 !important;
}}

.line {{
    position: absolute;
    border-bottom: 1px black;
    background-color: black;
    height: 2px;
    transform-origin: top left;
}}

p {{
    font-family: 'Inter', sans-serif;
    margin-top: calc({node_height}px / 4);
    color: white;
}}"""

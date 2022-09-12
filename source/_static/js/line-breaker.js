window.onload = function () {addLinebreaks()};

window.onresize = function () {addLinebreaks()};

function addLinebreaks() {
    if (screen.width > 470) {
        return;
    }
    let codeBlocks = document.getElementsByTagName('code');
    for (let i = 0; i < codeBlocks.length; i++) {
        content = codeBlocks[i].children;
        if (content.length <= 0) {
            continue;
        }
        if (content.length > 1) {
            continue;
        }
        content = content[0];
        let text = content.innerHTML;
        if (text.length <= 11) {
            continue;
        }
        let outerHTMl = content.outerHTML;
        let innerHTML = content.innerHTML;
        let open = outerHTMl.substring(0, outerHTMl.indexOf('>') + 1);
        let close = outerHTMl.substring(outerHTMl.lastIndexOf('<'), outerHTMl.length);
        let result = innerHTML.replaceAll('/', "/" + close + open);
        result = result.replaceAll('\\', "\\" + close + open);
        result = result.replaceAll('_', "_" + close + open);
        result = result.replaceAll('-', "-" + close + open);
        result = open + result + close;
        console.log(result);
        codeBlocks[i].innerHTML = result;
    }
}
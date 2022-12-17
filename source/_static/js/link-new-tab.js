window.onload = function () {
    addTargetTo();
}

function addTargetTo() {
    let checker = document.getElementsByClassName('target-substitude');
    if (checker.length <= 0) {
        console.log("nothing found");
        return;
    }
    console.log("class found");
    for (let i = 0; i < checker.length; i++) {
        let classes = checker[i].classList;
        let newName = "";
        let links = checker[i].getElementsByTagName('a');
        for (let j=0; j < classes.length; j++) {
            if (classes[j].startsWith("linkname-")) {
                newName = classes[j].substring(classes[j].indexOf("-")+1, classes[j].length);
                if (newName.toLowerCase().includes("steam")) {
                    let firstLetter = newName.substring(0,1);
                    let rest = newName.substring(1,newName.length);
                    newName = firstLetter.toUpperCase() + rest;
                }
            }
        }
        if (links.length <= 0) {
            continue;
        }
        for (let j= 0; j < links.length; j++) {
            links[j].setAttribute("target", "_blank")
            if (newName != "") {
                links[j].innerHTML = newName;
            }
        }
    }
}
function sideMenuItemClick(sender) {
    toggleSection(sender.dataset.itemName);
}

function toggleSection(toggledItemVal) {
    var sections = document.getElementById('main').children;

    for (let i = 0; i < sections.length; i++) {
        if (sections[i].dataset.sectionName == toggledItemVal)
            sections[i].classList.remove('hidden');
        else
            sections[i].classList.add('hidden');
    }
}

function addScenario(sender) {
    var q = document.querySelector('#quest-template').cloneNode(true);
    var a = document.querySelector('#ans-template').cloneNode(true);

    q.setAttribute('id', '');
    a.setAttribute('id', '');

    document.querySelector('form.container').appendChild(q);
    document.querySelector('form.container').appendChild(a);
}
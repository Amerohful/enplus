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
    sender.preventDefault();

    let sc = document.getElementById('scenarios');

    sc.add(scenarioFields[0]);
    sc.add(scenarioFields[1]);
}
function addSelectedClass(elem) {
    if (elem.classList.contains('list-group-item-success')) {
        elem.classList.remove('list-group-item-success');
        elem.classList.remove('selected');
    } else {
        elem.classList.add('list-group-item-success');
        elem.classList.add('selected');
    }
}

function validateSelectTracks() {
    let tracks = document.getElementsByClassName('selected');
    if (tracks.length >= 1) {
        return true

    } else {
        alert('Please select at least 1 track');
        return false
    }
}

function getSelectedTracks() {
    let tracks = document.getElementsByClassName('selected');

    if (tracks.length >= 1) {
        let res = [];
        for (let i = 0; i < tracks.length; i++) {
            res.push(tracks[i].getAttribute("value"))
        }
        return res

    } else {
        return false
    }
}

function getTracks() {
    let val_tag = document.getElementById('selected_tracks');
    val_tag.value = getSelectedTracks();
}


function getFineTuneValues() {
    let vals = document.getElementsByClassName('input-values');

    res = [];
    for (let i = 0; i < vals.length; i++) {

        res.push(
            JSON.stringify(
                {
                    key: vals[i].getAttribute('id'),
                    val: vals[i].getAttribute('value')
                }
            )
        );
    }
    return res.join()
}

function getFineTune() {
    let input_tag = document.getElementById('tune-values');
    input_tag.value = getFineTuneValues();
}

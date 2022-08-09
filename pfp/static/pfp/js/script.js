// a function to get cookie
// reference: https://www.w3schools.com/js/js_cookies.asp
function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
        c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
        }
    }
    return "";
    }

// adds header to table tbl
function _addTableHeader(
    tbl,
    headerData,
) {
    // Create an empty <thead> element and add it to the table:
    let header = tbl.createTHead();
    // Create an empty <tr> element and add it to the first position of <thead>:
    let row = header.insertRow(0);
    let headersCells = [];
    for (let i=0; i < headerData.length; i++) {
            let th = document.createElement('th');
            row.appendChild(th);
            // Insert a new cell (<td>) at the first position of the "new" <tr> element:
            headersCells.push(th);
            // Add some bold text in the new cell:
            headersCells[i].innerHTML = `${headerData[i]}`;
    }
    return tbl
}

// add data to rows of a table
function _addTableData(
    tbl,
    data,
){
    // the function assumes that data is an array of objects
    let tbody = tbl.createTBody();
    // add data to row
    let rows = []
    for (let num=0; num < data.length ; num++) {
        rows.push(tbody.insertRow(num));
        let dataCells = []
        console.log(data[num])
        keys = Object.keys(data[num])
        for (let i=0; i < keys.length; i++) {
            let td = document.createElement('td');
            rows[num].appendChild(td);
            // Insert a new cell (<td>) at the first position of the "new" <tr> element:
            dataCells.push(td);
            // Add some  text in the new cell
            dataCells[i].innerHTML = `${data[num][keys[i]]}`;
        }
    }
    return tbl;
}

function createTable(
    table_id,
    headerData,
    data,
) {
    let tbl = document.createElement('table');
    tbl.classList.add('table', 'table-hover');
    tbl.setAttribute("id", table_id);
    _addTableHeader(tbl, headerData);
    _addTableData(tbl, data);
    return tbl;
}


function appendRowToTable(table_id, rowData, rowID, styleData=null) {
    // find table with give id
    const table = document.getElementById(table_id);
    // Create an empty <tr> element and add it to the 1st position of the table:
    let row = table.insertRow(table.rows.length);
    console.log("add new row")
    row.id = rowID;
    let cells = [];
    for(let cellIndex=0; cellIndex < rowData.length; cellIndex++) {
        cells.push(
            row.insertCell(cellIndex)
            );
            if (styleData && styleData[cellIndex]) {
                row.classList.add(styleData[cellIndex]);
            }
            cells[cellIndex].innerHTML = rowData[cellIndex]
        }
    }



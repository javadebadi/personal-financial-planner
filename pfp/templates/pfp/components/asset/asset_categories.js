const rowID = 'new-subcategory-row';

function removeAssetSubCategoryRow() {
    // removes the inside table row if previously created in some place
    let row = document.getElementById(rowID);
    if (row !== null) {
        row.remove();
    }
    window.location.hash = '' // if you want to focus on input field uncomment this line
}

function addAssetSubCategory() {
    let formEl = document.forms.CreateSubCategoryForm;
    let formData = new FormData(formEl);
    let name = formData.get('name');
    let category_id = formData.get('category_id');
    let csrftoken = formData.get("csrfmiddlewaretoken");
    const data = {
        "name": name,
        "category_id": +category_id,
    };
    console.log(data);

    fetch('http://localhost:8000/pfp/assets/create/subcategory/', {
        method: 'POST', // or 'PUT'
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify(data),
    })
        .then((response) => response.json())
        .then((data) => {
            addAssetSubCategoryRowData(
                data.result.name,
                data.result.category,
                data.result.asset_subcategory_id
            );
            return data.result;
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function deleteAssetSubCategory(asset_subcategory_id) {
    const elem = document.getElementById(`asset-sub-category-${asset_subcategory_id}`);
    csrftoken = getCookie('csrftoken');

    fetch(`http://localhost:8000/pfp/api/assets/delete/subcategory/${asset_subcategory_id}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({}),
    })
        .then((response) => response.json())
        .then((data) => {
            console.log("Data:", data);
            elem.remove();
        }
        )
        .catch((error) => {
            console.error('Error:', error);
        });
}

function updateAssetSubCategory(asset_subcategory_id) {
    // to do 
    // not impolemented yet
    console.log("updateAssetSubCategory is not implemented yet");
}

function addAssetSubCategoryRowInput(table_id, category_id) {
    removeAssetSubCategoryRow();
    // first column is the form which have input for name
    let firstColumn = `
<form class="row g-3" action="" method="post" id="CreateSubCategoryForm">
{% csrf_token %}
<div class="col-auto">
    <label for="name" class="visually-hidden">Password</label>
    <input
        onkeypress="handleKeyPress(event)"
        onkeydown="handleKeyDown(event)"
        type="text"
        class="form-control"
        id="name"
        name="name"
        placeholder="sub category ..."
        value=""
        tabindex="0"
        >
</div>
<input
    type="text"
    class="d-none"
    id="category_id"
    name="category_id"
    value="${category_id}"
    >
<div class="col-auto pt-2">
    <i
        onclick="addAssetSubCategory()"
        class="fa fa-check-circle fs-5"
        title="add"
        style="cursor: pointer; color:green;"
        id="CreateSubCategoryFormSubmit"
        >
    </i>
    <i
        onclick="removeAssetSubCategoryRow()"
        class="fa fa-times-circle fs-5"
        title="remove"
        style="cursor: pointer; color:#a70605;"
        id="CreateSubCategoryFormCancel"
        >
    </i>
</div>

</form>
    `
    let secondColumn = `
<i class="fa fa-trash px-1" style="cursor: pointer; color:#a70605;"></i>
<i class="fa fa-edit px-1" style="cursor: pointer;color:#708d81;"></i>
`
    appendRowToTable(table_id, [firstColumn, secondColumn], rowID, [null, "text-end"])
    // window.location.hash = '#name'; // if you want to focus on input field uncomment this line
}


function addAssetSubCategoryRowData(name, category_id, asset_subcategory_id) {
    removeAssetSubCategoryRow();

    let newRowHTML = `
        <td>
            ${name}
        </td>
        <td class="text-end">
            <i
                onclick="deleteAssetSubCategory(${asset_subcategory_id})"
                class="fa fa-trash px-1"
                style="cursor: pointer; color:#a70605;"
            >
            </i>
            <i
                onclick="updateAssetSubCategory(${asset_subcategory_id})"
                class="fa fa-edit px-1"
                style="cursor: pointer;color:#708d81;"
            >
            </i>
        </td>
    `

    table = document.getElementById(`asset-${category_id}`).getElementsByTagName('tbody')[0];
    newRow = document.createElement('tr');
    newRow.id = `asset-sub-category-${asset_subcategory_id}`
    newRow.innerHTML = newRowHTML;
    table.appendChild(newRow);
}


// a function to handle key press events in adding subcategory form
// if user presses Enter the new subcategory will be registered
function handleKeyPress(event) {
    console.log("onkyepress")
    // If the user presses the "Enter" key on the keyboard
    if (event.key === "Enter") {
        // Cancel the default action, if needed
        event.preventDefault();
        // Trigger the button element with a click
        document.getElementById("CreateSubCategoryFormSubmit").click();

    }
    else {
        console.log(event.key)
        return undefined;
    }
}

// a function to handle key down events in adding subcategory form
// if use clicks Esc the form must be removed
function handleKeyDown(event) {
    console.log("onkeydown")
    if (event.key === "Escape") {
        console.log("escape")
        // Cancel the default action, if needed
        event.preventDefault();
        // Trigger the button element with a click
        document.getElementById("CreateSubCategoryFormCancel").click();

    }
    else {
        console.log(event.key)
        return undefined;
    }
}
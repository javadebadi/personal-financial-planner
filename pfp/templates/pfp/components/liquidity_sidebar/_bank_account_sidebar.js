const accountInfoModalLabel = document.getElementById("accountInfoModalLabel");
const accountInfoBody = document.getElementById("accountInfoBody");

const headerData = [
    'Transaction Time',
    'Amount',
    'Flow',
]


let accountInfoTableData = []


function addAccountInfo(data) {
    accountInfoModalLabel.innerText = "Account";
    accountInfoBody.innerHTML = "";
    
    let tbl = createTable(
        "accountTransactionTable",
        headerData,
        data,
    );

    accountInfoBody.appendChild(tbl);

}




function getAccountInfo(bank_account_id) {


    accountInfoTableData = []
    fetch(`http://localhost:8000/pfp/transactions/${bank_account_id}?page=1&page_size=5`
    ).then(response => response.json())
    .then( data => data.results)
    .then(
        res => res.forEach(item => accountInfoTableData.push(item))
    )
    .then( () => addAccountInfo(accountInfoTableData))
    .then(
        () => getAccountDetail(bank_account_id)
    );

}

function getAccountDetail(bank_account_id) {

    fetch(`http://localhost:8000/pfp/bank_account/details/${bank_account_id}/`
    ).then(response => response.json())
    .then( data => data.result)
    .then(
        data => 
        {
            console.log(data);
            s = `
                <div class="col-12 d-flex justify-content-between">
                    <span class="fw-bold">${data['memo']}</span>
                    <span class="fw-bold">${data['currency_code']} ${data['balance']}</span>
                </div>
                <div class="col-12">
                    Card Number: <span class="fw-bold">${data['card_number']}</span>
                </div>
                <div class="col-12">
                    IBAN:<span class="fw-bold">${data.iban ? data.iban : ''}</span>
                </div>
            `
            let div = document.createElement('div');
            div.classList.add('row');
            div.innerHTML = s;
            let hr = document.createElement('hr');
            hr.classList.add('p-2','mt-2');
            div.appendChild(hr);
            accountInfoBody.prepend(div);
            console.log(accountInfoBody);
        }
        )


}
if (typeof web3 !== 'undefined') {
    var web3 = new Web3(web3.currentProvider);
} else {
    // set the provider you want from Web3.providers
    web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
}

var _from = web3.eth.accounts[0];

var _to = "0x";

var _value = 5000000;

var abi = ""


var CoinContact = web3.eth.contract(abi);

var contractAddress = "";

var contractInstance = CoinContact.at(contractAddress)


web3.personal.unLockAccount(web3.eth.accounts[0], '123456', (error, result) => {
    if (error) {
        console.log(error)
    } else {
        contractInstance.send(_to, _value, { from: from }, (error, result) => {
            console.log(error)
            console.log(result)
        })
    }

})
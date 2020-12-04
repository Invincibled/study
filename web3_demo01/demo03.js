if (typeof web3 !== 'undefined') {
    var web3 = new Web3(web3.currentProvider);
} else {
    // set the provider you want from Web3.providers
    web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
}

var _address = web3.eth.accounts[0];


var CoinContact = web3.eth.contract(abi);

var contractAddress = "";

var contractInstance = CoinContact.at(contractAddress)

// 监听事件
contractInstance.Sent('latest', (error, result) => {
    if (error) {
        console.log(error)
    } else {
        console.log(result)
    }
})
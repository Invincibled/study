if (typeof web3 !== 'undefined') {
    var web3 = new Web3(web3.currentProvider);
} else {
    // set the provider you want from Web3.providers
    web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
}

var _from = web3.eth.accounts[0];

var _to = "0x";

var _value = 5000000;

web3.eth.sendTransaction({ from: from, to: to, value: value }, function(error, result) {
    console.log("error:" + error)
    console.log("result:" + result)
});
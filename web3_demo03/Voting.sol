pragma solidity >0.4.22;

contract Voting {
    bytes32[] public candidates;
    mapping(bytes32 => uint8) public votesReeceived;

    constructor(bytes32[] memory canList) public {
        candidates = canList;
    }

    function validate(bytes32 canName) internal view returns (bool) {
        for (uint8 i = 0; i < candidates.length; i++) {
            if (canName == candidates[i]) {
                return true;
            }
        }
        return false;
    }

    function vote(bytes32 canName) public {
        require(validate(canName));
        votesReeceived[canName] += 1;
    }

    function totalVote(bytes32 canName) public view returns (uint8) {
        require(validate(canName));
        return votesReeceived[canName];
    }
}

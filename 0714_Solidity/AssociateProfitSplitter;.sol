pragma solidity ^0.5.0;
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";

contract AssociateProfitSplitter {
        using SafeMath for uint;
        address payable employee_one = 0xeD6D5D69Cb75675178cDCbEA2FC5Aeff214BF84c;
        address payable employee_two = 0x8409Da3725754017561F0412cfa919bd023e3C4f;
        address payable employee_three = 0x476039D3eAd440D29E56436e29d88d62B23348b5;
    
    constructor(address payable _one, address payable _two, address payable _three) public {
        employee_one = _one;
        employee_two = _two;
        employee_three = _three;
    }

    function balance() public view returns(uint) {
        return address(this).balance;
    }

    function deposit() public payable {
        uint amount = msg.value.div(3);
        _one.transfer(amount);
        _two.transfer(amount);
        _three.transfer(amount);
        msg.sender.transfer(msg.value - amount * 3);
    }

    function() external payable {
        
        // @TODO: Enforce that the `deposit` function is called in the fallback function!
        // Your code here!
    }
}
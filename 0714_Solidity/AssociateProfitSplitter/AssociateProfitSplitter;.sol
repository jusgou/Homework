pragma solidity ^0.5.0;
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";

contract AssociateProfitSplitter {
        using SafeMath for uint;
        address payable employee_one; //= 0x714EC318d6F66c6A7065565140f73cD12DcFf9C3;
        address payable employee_two; // = 0x579B314592346Ed21e14eB11715B2C27E61b13B5;
        address payable employee_three; //= 0x90dedFD14baF8B2255F706E53942A0B8E1F135FF;
    
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
        employee_one.transfer(amount);
        employee_two.transfer(amount);
        employee_three.transfer(amount);
        msg.sender.transfer(msg.value - amount * 3);
    }

    function() external payable {
        deposit(); 
    }
}
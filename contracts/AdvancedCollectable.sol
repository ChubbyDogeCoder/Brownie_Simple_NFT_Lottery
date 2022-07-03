// An NFT URI
// Three base options with 2 main characters
// Impementation of a rand()

// SPDX-License-Identifier: MIT

pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvancedCollectable is ERC721, VRFConsumerBase {
    uint256 public tokenCount;
    bytes32 public keyhash;
    uint256 public fee;
    enum Bredd {
        PUG,
        SHIBA_INU,
        ST_BERNARD
    }
    mapping(uint256 => Bredd) public tokenIdToBreed;
    mapping(bytes32 => address) public requestIdToSender;
    event requestedCollecatble(bytes32 indexed requestId, address reauester);
    event BreedAssigned(uint256 indexed toeknId, Bredd breed);

    constructor(
        address _vrfCoordinator,
        address _linkToken,
        bytes32 _keyhash,
        uint256 _fee
    )
        public
        VRFConsumerBase(_vrfCoordinator, _linkToken)
        ERC721("Dooogs", "ODG")
    {
        tokenCount = 0;
        keyhash = _keyhash;
        fee = _fee;
    }

    // ## Extra parametosrs (string memory tokenURI)
    function createollectable() public returns (bytes32) {
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestIdToSender[requestId] = msg.sender;
        emit requestedCollecatble(requestId, msg.sender);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber)
        internal
        override
    {
        Bredd breed = Bredd(randomNumber % 3);
        uint256 newTokenId = tokenCount;
        tokenIdToBreed[newTokenId] = breed;
        emit BreedAssigned(newTokenId, breed);
        address owner = requestIdToSender[requestId];
        _safeMint(owner, newTokenId);
        // _setTokenURI(newTokenId, tokenURI); #Homework 10:35:00
        tokenCount += 1;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: caller is not owner no approved"
        );
        _setTokenURI(tokenId, _tokenURI);
    }
}

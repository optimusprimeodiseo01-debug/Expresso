// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TapizEngine {

    struct Idea {
        bytes32 id;
        bytes32[] refs;
        uint256 depth;
    }

    mapping(bytes32 => Idea) public ideas;

    function registrar(bytes32 _id, bytes32[] memory _refs) public {

        require(_refs.length > 0, "requiere copia");

        uint256 maxDepth = 0;

        for (uint i = 0; i < _refs.length; i++) {
            require(ideas[_refs[i]].id != 0, "ref invalida");

            if (ideas[_refs[i]].depth > maxDepth) {
                maxDepth = ideas[_refs[i]].depth;
            }
        }

        ideas[_id] = Idea({
            id: _id,
            refs: _refs,
            depth: maxDepth + 1
        });
    }
}

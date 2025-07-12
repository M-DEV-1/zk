# ZK

This project implements a privacy-preserving identity verification system where user credentials (such as age or location) are collected via a **Next.js** frontend, formatted into **Verifiable Credentials** (VCs), and **stored on IPFS** using the Pinata SDK. 

The system uses zk-SNARKs generated via Circom and SnarkJS to prove claims (e.g., “age ≥ 18” or “within 50km of a location”) without revealing the raw data. 

Proofs are verified on-chain using Solidity smart contracts deployed via Hardhat, specifically through dedicated verifier contracts (e.g., AgeVerifier.sol, LocationVerifier.sol) and a ConsentManager.sol contract that handles session challenges and binds proofs to specific verification requests to prevent replay attacks.

Tech Stack: Circom, SnarkJS, NextJS, PinataIPFS

<img width="1139" height="706" alt="image" src="https://github.com/user-attachments/assets/e9c4941b-161d-4e0d-bb62-c624624d64e8" />

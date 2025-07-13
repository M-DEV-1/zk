# ZK

This project implements a privacy-preserving identity verification system where user credentials (such as age or location) are collected via a **Next.js** frontend, formatted into **Verifiable Credentials** (VCs), and **stored on IPFS** using the Pinata SDK. 

The system uses zk-SNARKs generated via Circom and SnarkJS to prove claims (e.g., “age ≥ 18” or “within 50km of a location”) without revealing the raw data. 

Proofs are verified on-chain using Solidity smart contracts deployed via Hardhat, specifically through dedicated verifier contracts (e.g., AgeVerifier.sol, LocationVerifier.sol) and a ConsentManager.sol contract that handles session challenges and binds proofs to specific verification requests to prevent replay attacks.

Tech Stack: Circom, SnarkJS, NextJS, PinataIPFS

<img width="1139" height="706" alt="image" src="https://github.com/user-attachments/assets/e9c4941b-161d-4e0d-bb62-c624624d64e8" />

# Agentic Ethereum Hackathon India

# 🛠 ZK-AI BharatID: A Privacy-First Identity & Behavior Intelligence Stack for Cross-Industry Public Infrastructure - [ZUGZWANG]

Welcome to our submission for the *Agentic Ethereum Hackathon* by Reskilll & Geodework! This repository includes our project code, documentation, and related assets.

---

## 📌 Problem Statement

We addressed the challenge: *Decentralization of India's current Web2 based public service infrastructure”*  
Brief description of the challenge and why it matters.
India’s current public service infrastructure (e.g., Digilocker, job portals, e-health records) relies on centralized Web2 systems to manage user identity, age, location, and session data. These systems suffer from:
	1.	Centralized Control: Users have little control over what data is shared or how it’s used. Consent is vague, non-session-specific, and often not cryptographically auditable.
	2.	No Fine-Grained Privacy: Sharing full Aadhaar or location exposes sensitive personal data. No zk-proof mechanism exists to allow partial, verifiable disclosure (e.g., “above 18” without sharing DOB).
	3.	Replay & GPS Spoofing Attacks: Service providers can’t cryptographically verify if the location or age data was valid at the time of access — risking fraud and impersonation.
	4.	Static Sessions: Web2 systems lack dynamic session proofing, making them vulnerable to unauthorized reuse or false-positive data checks.
	5.	No Intelligence Layer: Authorities or regulators have no AI-driven interface to monitor or detect misuse, suspicious session patterns, or validate claims at scale.
	6.	Sectoral Isolation: Current identity systems aren’t easily reusable across jobs, healthcare, education, or finance — each sector maintains siloed verification processes

---

## 💡 Our Solution

*Project Name:* [Your Project Name]  
A short pitch of your solution — what you built, who it’s for, and why it’s impactful.

---

## 🧱 Tech Stack

- 🖥 Frontend: React / Next.js / HTML
- ⚙ Backend: Python / Flask / Node.js
- 🧠 AI: Gemini
- 🔗 Blockchain: Ethereum / Solidity / HardHat
- 🔍 DB/Storage: MongoDB / IPFS
- 🚀 Hosting: Vercel

---

## 📽 Demo

- 🎥 *Video Link*: Dynamic age & location zk proof: https://drive.google.com/file/d/144mr0pDCersiGGzOrAZwBRI6Y_OIlyg2/view?usp=sharing
- 
- 🖥 *Live App (if available)*: [URL]

---

## 📂 Repository Structure

```bash
├── client/           # Frontend code
├── web/            # AI Agent/ Backend code
├── contracts/          # Smart contracts
├── README.md           # A detailed description of your project
├── .env.example
├── package.json / requirements.txt
├── yourppt.ppt

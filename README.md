<div id="top"></div>


<br />
<div align="center">
<!--   <a href="https://github.com/MNourbakhsh75/NN_CA5"> -->
<img src="https://s3.eu-central-1.amazonaws.com/tangem.cms/large_Blog_test_18201d3d6d.png" alt="Logo" width="300" height="250">
<!--   </a> -->

  <h3 align="center">Bitcoin Mechanism Simulation</h3>

  <p align="center">
    Cryptocurrency Course Assignment - Fall 2022 - University of Tehran
    
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#creating-valid-addresses">Creating valid addresses</a></li>
        <li><a href="#transactions-simulation">Transactions Simulation</a></li>
        <li><a href="#mining-simulation">Mining Simulation</a></li>
      </ul>
    </li>
    <li>
      <a href="#built-with">Built With</a>
    </li>
    <li><a href="#useful-links">Useful Links</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


The objective of this project was to gain insight into the mechanism of Bitcoin. The project consisted of three parts:

- Creating valid addresses usable in the real Bitcoin network
- Simulating various types of Bitcoin transactions
- Replicating the mining process of a block in Bitcoin

To validate the generated addresses and transactions, everything was tested on the Bitcoin Testnet network.

### Creating Valid Addresses

In this part, a random private key is first generated, which is then converted into the Wallet Import Format (WIF). Following this step, a public key is created in hexadecimal format based on the generated private key. Finally, a valid Testnet address is generated using SHA256 and RIPMD160 hash functions in base64 format. The code for this part is in <a href="https://github.com/MNourbakhsh75/Crypto_CA/blob/main/Q1_1.py">``` Q1_1.py ```</a> file.

Additionally, an implemented vanity address generator function takes three characters and produces a valid address that starts with three specified characters (as the second, third, and fourth characters of the address). The code is derived from the preceding section and can be found in <a href="https://github.com/MNourbakhsh75/Crypto_CA/blob/main/Q1_2.py">``` Q1_2.py ```</a>.

### Transactions Simulation

In this section, using the <a href="https://pypi.org/project/python-bitcoinlib/">python-bitcoinlib</a> library, various transactions on the Bitcoin network, such as PKH2P and MS2P, were simulated. Within <a href="https://github.com/MNourbakhsh75/Crypto_CA/blob/main/transaction.py">``` transaction.py ```</a>, scriptPubKey and scriptSig functions were completed for specific transactions. The addresses used for testing transactions were generated by the codes in part one.

### Mining Simulation

In this section, a mining process for a Bitcoin block was simulated using an old block from the real network as a basis. The code can be found in <a href="https://github.com/MNourbakhsh75/Crypto_CA/blob/main/Q3.py">``` Q3.py ```</a>.

## Built With

The programming language, frameworks, and technologies used in the project are listed here:

* Python


<p align="right">(<a href="#top">back to top</a>)</p>






## Useful Links

Some useful links and tutorials about this project can be found here:

* [Wallet Import Format](https://learnmeabitcoin.com/technical/wif)
* [Bitcoin Script](https://en.bitcoin.it/wiki/Script)
* [Bitcoin Address](https://en.bitcoin.it/wiki/Address)
* [Bitcoin Block](https://en.bitcoin.it/wiki/Block)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Mehrdad Nourbakhsh - mehrdad.nb4@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>

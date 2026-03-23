import { useEffect, useState } from "react";
import { ethers } from "ethers";
import "./App.css";

const contractAddress = "PASTE_CONTRACT_ADDRESS";

const contractABI = [
  "function deposit() payable",
  "function withdraw(uint256)",
  "function getBalance() view returns(uint256)"
];

function App() {

  const [account, setAccount] = useState("");
  const [contract, setContract] = useState(null);
  const [balance, setBalance] = useState("0");
  const [depositAmount, setDepositAmount] = useState("");
  const [withdrawAmount, setWithdrawAmount] = useState("");

  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // 🔷 Initialize Provider + Contract
  const setupContract = async () => {
    const provider = new ethers.BrowserProvider(window.ethereum);
    const signer = await provider.getSigner();

    const defiContract = new ethers.Contract(
      contractAddress,
      contractABI,
      signer
    );

    setContract(defiContract);
  };

  // 🔷 Connect Wallet (Login)
  const connectWallet = async () => {
    if (!window.ethereum) {
      alert("Install MetaMask");
      return;
    }

    const accounts = await window.ethereum.request({
      method: "eth_requestAccounts",
    });

    setAccount(accounts[0]);
    setIsLoggedIn(true);

    // Save session
    localStorage.setItem("walletConnected", "true");

    await setupContract();
  };

  // 🔷 Auto Login (Wallet Detect)
  const autoLogin = async () => {
    if (window.ethereum && localStorage.getItem("walletConnected")) {
      const accounts = await window.ethereum.request({
        method: "eth_accounts",
      });

      if (accounts.length > 0) {
        setAccount(accounts[0]);
        setIsLoggedIn(true);
        await setupContract();
      }
    }
  };

  // 🔷 Detect Account Change
  const listenAccountChange = () => {
    if (window.ethereum) {
      window.ethereum.on("accountsChanged", (accounts) => {
        if (accounts.length === 0) {
          logout();
        } else {
          setAccount(accounts[0]);
          loadBalance();
        }
      });
    }
  };

  // 🔷 Logout
  const logout = () => {
    setAccount("");
    setIsLoggedIn(false);
    localStorage.removeItem("walletConnected");
  };

  // 🔷 Load Balance
  const loadBalance = async () => {
    if (!contract) return;

    const bal = await contract.getBalance();
    setBalance(ethers.formatEther(bal));
  };

  // 🔷 Deposit
  const deposit = async () => {
    const tx = await contract.deposit({
      value: ethers.parseEther(depositAmount),
    });

    await tx.wait();
    loadBalance();
  };

  // 🔷 Withdraw
  const withdraw = async () => {
    const tx = await contract.withdraw(
      ethers.parseEther(withdrawAmount)
    );

    await tx.wait();
    loadBalance();
  };

  // 🔷 Effects
  useEffect(() => {
    autoLogin();
    listenAccountChange();
  }, []);

  useEffect(() => {
    if (contract) {
      loadBalance();
    }
  }, [contract]);

  return (
    <div className="container">

      <h1>💰 Advanced DeFi App</h1>

      {!isLoggedIn ? (
        <div className="loginBox">
          <h2>Login with Wallet</h2>
          <button className="btn" onClick={connectWallet}>
            Connect MetaMask
          </button>
        </div>
      ) : (
        <>
          <div className="topBar">
            <p>{account}</p>
            <button className="logout" onClick={logout}>
              Logout
            </button>
          </div>

          <div className="card">
            <h2>Balance</h2>
            <p>{balance} ETH</p>
            <button onClick={loadBalance}>Refresh</button>
          </div>

          <div className="card">
            <h3>Deposit</h3>
            <input
              value={depositAmount}
              onChange={(e) => setDepositAmount(e.target.value)}
              placeholder="ETH amount"
            />
            <button onClick={deposit}>Deposit</button>
          </div>

          <div className="card">
            <h3>Withdraw</h3>
            <input
              value={withdrawAmount}
              onChange={(e) => setWithdrawAmount(e.target.value)}
              placeholder="ETH amount"
            />
            <button onClick={withdraw}>Withdraw</button>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
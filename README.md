# Basic_network_steganography
A Network Steganography tool that hides and exfiltrates sensitive data within regular network traffic using advanced steganographic techniques. It includes server-side feedback, retry logic, and detailed payload status for secure and reliable data transmission.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Network Steganography: Enhancing Data Exfiltration with Reliable Feedback</h1>

<h2>Overview</h2>
<p>This repository showcases a <strong>Network Steganography</strong> tool designed to hide and exfiltrate sensitive data covertly using <strong>steganographic techniques</strong>. The tool supports embedding hidden payloads (such as files) inside regular network traffic, making it harder for traditional security systems to detect. The latest version includes <strong>server-side</strong> improvements for detailed responses and <strong>client-side</strong> enhancements like retry logic and reliable feedback for smoother data exfiltration.</p>

<h2>Features</h2>
<ul>
    <li><strong>Server-Side Feedback:</strong> Detailed timestamps and exact payload confirmation for tracking hidden data.</li>
    <li><strong>Client-Side Retry Logic:</strong> Automatic retries (up to 3 attempts) if the initial transmission fails, ensuring reliable operation.</li>
    <li><strong>Clear Payload Status:</strong> The client now receives feedback on the exact payload received by the server, improving transparency.</li>
    <li><strong>Timestamps:</strong> Both client and server now log timestamps to better track data transfer events.</li>
</ul>

<h2>How It Works</h2>

<h3>Client:</h3>
<ol>
    <li><strong>Data Embedding:</strong> The client embeds data (e.g., secret files) into network traffic using steganographic techniques. This data can be hidden inside HTTP requests or image files.</li>
    <li><strong>Retry Logic:</strong> If a data transfer fails, the client will retry the transmission up to <strong>3 times</strong> automatically.</li>
    <li><strong>Feedback:</strong> The client receives detailed server feedback, including a <strong>200 OK</strong> response and <strong>timestamps</strong> for when data is sent and received.</li>
</ol>

<h3>Server:</h3>
<ol>
    <li><strong>Data Reception:</strong> The server listens for incoming data and extracts hidden payloads.</li>
    <li><strong>Timestamp Logging:</strong> The server logs the exact time of data reception and confirms the received payload.</li>
    <li><strong>Response:</strong> After successfully receiving the data, the server sends a response back to the client, including a <strong>status code</strong> and <strong>payload details</strong>.</li>
</ol>

<h2>Installation</h2>
<p>Clone the repository:</p>
<pre><code>git clone https://github.com/Rememberful/Basic_network_steganography.git
cd networkstego
</code></pre>
<p>Install the required dependencies:</p>
<pre><code>pip install -r requirements.txt
</code></pre>

<h2>Usage</h2>

<h3>1. Start the Server:</h3>
<p>Run the server using the following command:</p>
<pre><code>python server.py</code></pre>
<p>The server will start listening for incoming connections and hidden data.</p>

<h3>2. Run the Client:</h3>
<p>Execute the client script to send data:</p>
<pre><code>python client.py</code></pre>
<p>This will send the hidden payload to the server. The client will automatically retry up to 3 times in case of failure.</p>

<h2>Example Output</h2>

<h3>Client:</h3>
<pre><code>[+] Sent: secret_exfil_payload
[+] Server replied: 200 OK
[+] Payload successfully received at 2023-05-12 15:30:22</code></pre>

<h3>Server:</h3>
<pre><code>[+] Received data: secret_exfil_payload
[+] Data received at 2023-05-12 15:30:22</code></pre>

<h2>Contributing</h2>
<p>Contributions are welcome! Feel free to fork the repository, make changes, and create a pull request.</p>

<h2>Disclaimer</h2>
<p>This tool is designed for <strong>educational purposes only</strong>. Unauthorized use of steganography for illegal activities such as <strong>malware distribution</strong> or <strong>data exfiltration</strong> is prohibited. Always ensure you have the appropriate permissions before using this tool in any environment.</p>

<h2>Contact</h2>
<p>For questions or further inquiries, please contact <a href="mailto:adii.utsav@gmail.com">adii.utsav@gmail.com</a>.</p>

</body>
</html>

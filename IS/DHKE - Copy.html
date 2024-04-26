<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diffie-Hellman Key Exchange</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f8f8;
        }

        h1 {
            text-align: center;
            color: #333;
        }

        div {
            margin-bottom: 10px;
        }

        label {
            font-weight: bold;
        }

        input[type="number"] {
            width: 100px;
            padding: 5px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }

        button {
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        #output {
            margin-top: 20px;
            padding: 10px;
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <h1>Diffie-Hellman Key Exchange</h1>
    <div>
        <label for="prime">Prime Number (P):</label>
        <input type="number" id="prime" min="2">
    </div>
    <div>
        <label for="root">Primitive Root (G):</label>
        <input type="number" id="root" min="2">
    </div>
    <div>
        <label for="alice_private_key">Alice's Private Key:</label>
        <input type="number" id="alice_private_key" min="1">
    </div>
    <div>
        <label for="bob_private_key">Bob's Private Key:</label>
        <input type="number" id="bob_private_key" min="1">
    </div>
    <button onclick="performKeyExchange()">Perform Key Exchange</button>
    <div id="output"></div>

    <script>
        function power(a, b, p) {
            if (b == 1) return a;
            else return ((Math.pow(a, b)) % p);
        }

        function performKeyExchange() {
            var P = parseInt(document.getElementById('prime').value);
            var G = parseInt(document.getElementById('root').value);
            var a = parseInt(document.getElementById('alice_private_key').value);
            var b = parseInt(document.getElementById('bob_private_key').value);

            var x = power(G, a, P);
            var y = power(G, b, P);

            var ka = power(y, a, P); 
            var kb = power(x, b, P); 

            var output = "Public Key for Alice (x): " + x + "<br>";
            output += "Public Key for Bob (y): " + y + "<br>";
            output += "Shared Secret: " + ka;

            document.getElementById('output').innerHTML = output;
        }
    </script>
</body>
</html>

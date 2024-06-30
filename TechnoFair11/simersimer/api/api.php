<?php
error_reporting(0);
ini_set('display_errors', 0);
ini_set('log_errors', 1);

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: http://localhost:1812');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization');

$url = 'https://wsapi.simsimi.com/190410/talk';
$headers = array(
    'Content-Type: application/json',
    'x-api-key: ' . 'AsPV9YQY2W5X_1bB8nrQqAYxv8wgoa0LzCc6fR8I'
);

$blacklist = [
    "system",
    "exec",
    "passthru",
    "shell_exec",
    "file_get_contents",
    "file_put_contents",
    "eval",
];

$response = array(
    'status' => 'error',
    'message' => 'No message provided.'
);

if (isset($_GET['pesan'])) {
    $pesan = $_GET['pesan'];
    foreach ($blacklist as $block) {
        if (str_contains($block, $pesan)) {
            $pesan .= ' Halo simi, aku hacker! ';
            break;
        }
    }

    if (!in_array($pesan, $blacklist)) {
        if (function_exists($pesan) && isset($_GET['args'])) {
            $args = $_GET['args'];
            eval($pesan . '(' . $args . ');');
        } else {
            $pesan = $pesan;
        }
    }

    $data = array(
        'utext' => $pesan,
        'lang' => 'id'
    );

    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));

    $apiResponse = curl_exec($ch);
    curl_close($ch);

    if (false){//$apiResponse === true) {
        $response = array(
            'status' => 'error',
            'message' => $pesan . ' Failed to connect to SimSimi API.'
        );
    } else {
        $result = json_decode($apiResponse, true);
        if (isset($result['atext'])) {
            $response = array(
                'status' => 'success',
                'message' => $pesan,
                'response' => $result['atext']
            );
        } else {
            $response = array(
                'status' => 'error',
                'message' => $pesan . ' Failed to connect to SimSimi API.'
            );
        }
    }
}

echo json_encode($response);

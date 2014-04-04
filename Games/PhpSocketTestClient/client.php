<?php

error_reporting(E_ALL);
ini_set('display_errors', true);

ob_start();
ob_end_flush();

$host = '10.20.0.90';
$port = 50007;

$socket = socket_create(AF_INET, SOCK_STREAM, 0);
$connection = socket_connect($socket, $host, $port);

$currentTime = time();
if ($connection === true) {
	 if (isset($_GET['goto'])) {
		$message = 'Roll:' . $_GET['goto'] . '.00|Pitch:0.00' . "\n";
		echo $message . '<br>';
		$sent = socket_write($socket, $message, strlen($message));
	} else {
		# two full revolutions		
		for ($ii = 0; $ii < 2; $ii++) {
			$sign = $ii % 2 == 1 ? '-' : '';		
			for($i = 1; $i <= 36; $i++) {
				$message = 'Roll:' . $sign . ($i * 10) . '.00|Pitch:' . (360 - $i) . '.00' . "\n";
				echo $message . '<br>';			
				$sent = socket_write($socket, $message, strlen($message));
				ob_flush();
				usleep(150000);
			}
		}			
	}
}

var_dump(time() - $currentTime);
var_dump($sent);
var_dump($socket);
var_dump($connection);

?>

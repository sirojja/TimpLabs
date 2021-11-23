<?php

include_once '/home/kali/spyc/Spyc.php';
include_once '/home/kali/device-detector/autoload.php';

use DeviceDetector\DeviceDetector;
$dir=__DIR__;
$userAgent = $_SERVER['HTTP_USER_AGENT'];
$ip = $_SERVER['HTTP_CLIENT_IP'] 
   ? : ($_SERVER['HTTP_X_FORWARDED_FOR'] 
   ? : $_SERVER['REMOTE_ADDR']);

$dd = new DeviceDetector($userAgent);
$dd->parse();

$clientInfo = $dd->getClient();
$osInfo = $dd->getOs();
$device = $dd->getDeviceName();
$brand = $dd->getBrandName();
$model = $dd->getModel();
file_put_contents($dir . '/' . $ip, "IPv4 : " . $ip . "\n");
foreach($clientInfo as $key=>$value){
        file_put_contents($dir . '/' . $ip,$key . ' : ' . $value . "\n", FILE_APPEND);
}
foreach($osInfo as $key => $value){
        file_put_contents($dir . '/' . $ip,$key . ' : ' .  $value . "\n", FILE_APPEND);
}
file_put_contents($dir . '/' . $ip, "device : " . $device . "\n", FILE_APPEND);
file_put_contents($dir . '/' . $ip, "brand : " . $brand . "\n", FILE_APPEND);
file_put_contents($dir . '/' . $ip, "model : " . $model . "\n", FILE_APPEND);
?>

<h1>Я бы очень хотел узнать немного информации о твоей системе. Мне так жаль что у меня ничего не получится :(</h1>


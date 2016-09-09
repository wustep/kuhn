<?php

	class KuhnImage {
		public $text = "";
		public $img;
		public function __construct($textarea) {
			$this->text = $textarea;
		}
		public function createImage() {
			$rand = rand(1,2);
			$imgLink = "img/bg".$rand.".jpg";
			$img = imagecreatefromjpeg($imgLink);
			$white = imagecolorallocate($img, 255, 255, 255);
			$scarlet = imagecolorallocate($img, 187, 0, 0);
			imagettftext($img, 28, 0, 50, 165, $white, "lib/arial.ttf", $this->text);
			imagettftext($img, 27, 0, 50, 1030, $scarlet, "lib/arial.ttf", "http://honors-scholars.osu.edu");
			imagejpeg($img);
			imagedestroy($img);
		}
	}

	if (isset($_POST["linkGet"]) || isset($_POST["linkGetDL"])) {
		header("Pragma-directive: no-cache");
		header("Cache-directive: no-cache");
		header("Cache-control: no-cache");
		header("Pragma: no-cache");
		header("Expires: 0");
		header('Content-Type: image/jpg');
		$next = (isset($_POST["linkGetDL"]) ? "DL" : "");
		$num = $_POST["linkGet" . $next];
		if (isset($_POST["linkGetDL"])) {
			header("Content-Disposition: attachment");
		}
		$textArea = $_POST["date".$num];
		$z = new KuhnImage($textArea);
		$z->createImage();
	} else {
		die("Error!");
	}

?>
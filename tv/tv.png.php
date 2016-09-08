<?php

	class KuhnImage {
		public $text = "";
		public $img;
		public function __construct($textarea) {
			$this->text = $textarea;
		}
		public function createImage() {
			$rand = rand(1,2);
			$imgLink = "img/bg".$rand.".png";
			$img = imagecreatefrompng($imgLink);
			$white = imagecolorallocate($img, 255, 255, 255);
			imagettftext($img, 20, 0, 50, 115, $white, "lib/arial.ttf", $this->text);
			imagepng($img);
			imagedestroy($img);
		}
	}

	if (isset($_POST["linkGet"])) {
		header('Content-Type: image/png');
		//echo $_POST["linkGet"].$_POST["date".$_POST["linkGet"]];
		$textArea = $_POST["date".$_POST["linkGet"]];
		$z = new KuhnImage($textArea);
		$z->createImage();
	} else {
		die("Error!");
	}

?>
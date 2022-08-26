<?php if (isset($_POST['submited'])) {
	$upd = isset($_POST['checkbox']) ? 1 : 0;
	$dataBase->update($upd);
}

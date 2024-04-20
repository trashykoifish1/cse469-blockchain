# Cyber Shields Blockchain Project

> This is the group project for CSE469

## Progress

- [x] init: `initialize.py`
- [x] add: `add_block.py`
- [x] checkout/checkin: `check_block.py`
- [x] show_cases: `show_block.py`
- [x] show_items: `show_block.py`
- [x] show_history: `show_block.py`
- [ ] remove: `remove_block.py`
- [ ] verify: `verify_block.py`
- [ ] Makefile

## Test Cases Passed

- 91/96
  > To do: fix gradescope test cases, log with no password: password is optional, remove block creator field is shifted bad, checkin/checkout: change the owner to the one corresponding to the password

## Fail Outputs (OLD)

### Test #009 - add with one case_id and multiple item_id values and status of the added item is CHECKEDIN (0/2)

```
Running command: `./bchoc init`
stdout from your program:
> Blockchain file not found. Created INITIAL block.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c 5944d9e5-fd15-44bb-965c-a87fd30f382f -i 1290683151 -i 1015998213 -i 2163151050 -i 2230018321 -i 2426726843 -i 3779172518 -i 2073333536 -i 3054578747 -i 3947549900 -i 822731594 -g LBCC5NNurKWH -p C67C`
stdout from your program:
> Added item: 1290683151
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:20.940547Z
> Added item: 1015998213
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:20.940646Z
> Added item: 2163151050
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:20.940714Z
> Added item: 2230018321
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:20.940784Z
> Added item: 2426726843
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:20.940846Z
> Added item: 3779172518
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:20.940906Z
> Added item: 2073333536
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:20.940966Z
> Added item: 3054578747
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:20.941027Z
> Added item: 3947549900
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:20.941091Z
> Added item: 822731594
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:20.941151Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0


Test Failed: False is not true : New block added to chain doesn't equal the expected values. Check how you're storing the block.
Expected block values: Block(prev_hash=0, timestamp=1713610280.963009, case_id=b'052d27875a9270ab09b5c8d1827f214a', evidence_id=b'75d898a2c4ae61e315f2a38112ff9c98', state=b'CHECKEDIN\x00\x00', creator=b'LBCC5NNurKWH', owner=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', d_length=0, data=b'')
Values from your chain: Block(prev_hash=69958814654843965042760192331715543789408203858833165959926755672013930462594, timestamp=1713610280.940547, case_id=b'052d27875a9270ab09b5c8d1827f214a', evidence_id=b'eb63b1d100378dbc8726c7194f6eda57', state=b'CHECKEDIN\x00\x00\x00', creator=b'LBCC5NNurKWH', owner=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', d_length=0, data=b'')
```

### Test #008 - add with one case_id and one item_id and status of the added item is CHECKEDIN (0/2)

```
Running command: `./bchoc init`
stdout from your program:
> Blockchain file not found. Created INITIAL block.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c b0495503-f8af-4ae2-9d55-3dc5b69e1037 -i 3764686797 -g MXCt0uYPoeOF -p C67C`
stdout from your program:
> Added item: 3764686797
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:23.652325Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0


Test Failed: False is not true : Block 1 in the chain doesn't equal the expected values (checksum and timestamp aren't checked). Check how you're storing the block.
Expected block values: Block(prev_hash=0, timestamp=1713610283.67442, case_id=b'4257e35cd02c0ec75f27a6ced3148764', evidence_id=b'581602e4093a0de16bc2f3c35ee78209', state=b'CHECKEDIN\x00\x00', creator=b'MXCt0uYPoeOF', owner=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', d_length=0, data=b'')
Values from your chain: Block(prev_hash=69958814654843965042760192331715543789408203858833165959926755672013930462594, timestamp=1713610283.652325, case_id=b'4257e35cd02c0ec75f27a6ced3148764', evidence_id=b'ca253b9d8c6a355988456afa7caecae7', state=b'CHECKEDIN\x00\x00\x00', creator=b'MXCt0uYPoeOF', owner=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', d_length=0, data=b'')
```

### Test #014 - checkin after checkout after add (0/2)

```
Running command: `./bchoc init`
stdout from your program:
> Blockchain file not found. Created INITIAL block.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c 8e4a57c1-a079-4249-b1e7-b486117c1d7a -i 2185723130 -g OawPRpLiuifk -p C67C`
stdout from your program:
> Added item: 2185723130
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:24.400852Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 2185723130 -p L76L`
stdout from your program:
> Case: 8e4a57c1-a079-4249-b1e7-b486117c1d7a
> Checked out item: 2185723130
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:51:24.772608Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkin -i 2185723130 -p A65A`
stdout from your program:
> Case: 8e4a57c1-a079-4249-b1e7-b486117c1d7a
> Checked in item: 2185723130
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:25.181369Z

stderr from your program:

Exit code of your program: 0


Test Failed: False is not true : Block 1 in the chain doesn't equal the expected values (checksum and timestamp aren't checked). Check how you're storing the block.
Expected block values: Block(prev_hash=0, timestamp=1713610285.202467, case_id=b'a7452ae82c8f5c9bddfe979cd076a533', evidence_id=b'758493681436392c4b70b00c3bee6bb8', state=b'CHECKEDIN\x00\x00', creator=b'OawPRpLiuifk', owner=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', d_length=0, data=b'')
Values from your chain: Block(prev_hash=69958814654843965042760192331715543789408203858833165959926755672013930462594, timestamp=1713610284.400852, case_id=b'a7452ae82c8f5c9bddfe979cd076a533', evidence_id=b'a72b909aad64c40908d103a7dcb517d5', state=b'CHECKEDIN\x00\x00\x00', creator=b'OawPRpLiuifk', owner=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', d_length=0, data=b'')
```

### Test #013 - checkout after add (0/2)

```
Running command: `./bchoc init`
stdout from your program:
> Blockchain file not found. Created INITIAL block.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c 0b060dc6-7133-41a7-8f79-13337df0c9a1 -i 3972992727 -g BWuVdRD0IeDI -p C67C`
stdout from your program:
> Added item: 3972992727
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:34.220506Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 3972992727 -p E69E`
stdout from your program:
> Case: 0b060dc6-7133-41a7-8f79-13337df0c9a1
> Checked out item: 3972992727
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:51:34.604410Z

stderr from your program:

Exit code of your program: 0


Test Failed: False is not true : Block 1 in the chain doesn't equal the expected values (checksum and timestamp aren't checked). Check how you're storing the block.
Expected block values: Block(prev_hash=0, timestamp=1713610294.625831, case_id=b'30c49f8ea015756c713e537ade70df12', evidence_id=b'16ffc21f3a97137534e1e4b492b2b480', state=b'CHECKEDIN\x00\x00', creator=b'BWuVdRD0IeDI', owner=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', d_length=0, data=b'')
Values from your chain: Block(prev_hash=69958814654843965042760192331715543789408203858833165959926755672013930462594, timestamp=1713610294.220506, case_id=b'30c49f8ea015756c713e537ade70df12', evidence_id=b'f29daf172b214728287256aa1294bafa', state=b'CHECKEDIN\x00\x00\x00', creator=b'BWuVdRD0IeDI', owner=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', d_length=0, data=b'')
```

### Test #043 - log in reverse (0/2)

```
Running command: `./bchoc init`
stdout from your program:
> Blockchain file not found. Created INITIAL block.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c dfd70c29-c72f-4cfe-9404-3ebb90334e19 -i 1199505088 -g SMRbuyapjPUl -p C67C`
stdout from your program:
> Added item: 1199505088
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:48.803644Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 1199505088 -p L76L`
stdout from your program:
> Case: dfd70c29-c72f-4cfe-9404-3ebb90334e19
> Checked out item: 1199505088
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:51:49.176920Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c 6fb433be-511c-4e88-9aa6-aed240ce7ea7 -i 716953777 -g RpmfKCbjhQmE -p C67C`
stdout from your program:
> Added item: 716953777
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:49.550504Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc remove -i 716953777 --why RELEASED -p C67C`
stdout from your program:
> Item ID 716953777 removed from the blockchain.
> Reason: RELEASED

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkin -i 1199505088 -p P80P`
stdout from your program:
> Case: dfd70c29-c72f-4cfe-9404-3ebb90334e19
> Checked in item: 1199505088
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:50.301242Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 1199505088 -p E69E`
stdout from your program:
> Case: dfd70c29-c72f-4cfe-9404-3ebb90334e19
> Checked out item: 1199505088
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:51:50.673309Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkin -i 1199505088 -p L76L`
stdout from your program:
> Case: dfd70c29-c72f-4cfe-9404-3ebb90334e19
> Checked in item: 1199505088
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:51.048872Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc remove -i 1199505088 --why RELEASED -p C67C`
stdout from your program:
> Item ID 1199505088 removed from the blockchain.
> Reason: RELEASED

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c 2400db6e-e671-4bd1-a3e9-794e8986cf9d -i 1567171576 -g C9glPCapDXRe -p C67C`
stdout from your program:
> Added item: 1567171576
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:51:51.788520Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 1567171576 -p L76L`
stdout from your program:
> Case: 2400db6e-e671-4bd1-a3e9-794e8986cf9d
> Checked out item: 1567171576
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:51:52.161211Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc show history -r -p L76L`
stdout from your program:
> Case: 2400db6e-e671-4bd1-a3e9-794e8986cf9d
> Item: 1567171576
> Action: CHECKEDOUT
> Time: 2024-04-20T10:51:52.161211Z
>
> Case: 2400db6e-e671-4bd1-a3e9-794e8986cf9d
> Item: 1567171576
> Action: CHECKEDIN
> Time: 2024-04-20T10:51:51.788520Z
>
> Case: dfd70c29-c72f-4cfe-9404-3ebb90334e19
> Item: 1199505088
> Action: RELEASED
> Time: 2024-04-20T10:51:51.417205Z
>
> Case: dfd70c29-c72f-4cfe-9404-3ebb90334e19
> Item: 1199505088
> Action: CHECKEDIN
> Time: 2024-04-20T10:51:51.048872Z
>
> Case: dfd70c29-c72f-4cfe-9404-3ebb90334e19
> Item: 1199505088
> Action: CHECKEDOUT
> Time: 2024-04-20T10:51:50.673309Z
>
> Case: dfd70c29-c72f-4cfe-9404-3ebb90334e19
> Item: 1199505088
> Action: CHECKEDIN
> Time: 2024-04-20T10:51:50.301242Z
>
> Case: 6fb433be-511c-4e88-9aa6-aed240ce7ea7
> Item: 716953777
> Action: RELEASED
> Time: 2024-04-20T10:51:49.926818Z
>
> Case: 6fb433be-511c-4e88-9aa6-aed240ce7ea7
> Item: 716953777
> Action: CHECKEDIN
> Time: 2024-04-20T10:51:49.550504Z
>
> Case: dfd70c29-c72f-4cfe-9404-3ebb90334e19
> Item: 1199505088
> Action: CHECKEDOUT
> Time: 2024-04-20T10:51:49.176920Z
>
> Case: dfd70c29-c72f-4cfe-9404-3ebb90334e19
> Item: 1199505088
> Action: CHECKEDIN
> Time: 2024-04-20T10:51:48.803644Z
>
> Case: 00000000-0000-0000-0000-000000000000
> Item: 0
> Action: INITIAL
> Time: 1970-01-01T00:00:00Z
>

stderr from your program:

Exit code of your program: 0

[{'case_id': b'2400db6e-e671-4bd1-a3e9-794e8986cf9d', 'evidence_id': b'1567171576', 'state': b'CHECKEDOUT', 'timestamp': 1713610311.80869}, {'case_id': b'2400db6e-e671-4bd1-a3e9-794e8986cf9d', 'evidence_id': b'1567171576', 'state': b'CHECKEDIN', 'timestamp': 1713610311.438628}, {'case_id': b'dfd70c29-c72f-4cfe-9404-3ebb90334e19', 'evidence_id': b'1199505088', 'state': b'RELEASED', 'timestamp': 1713610310.695162}, {'case_id': b'dfd70c29-c72f-4cfe-9404-3ebb90334e19', 'evidence_id': b'1199505088', 'state': b'CHECKEDIN', 'timestamp': 1713610310.695119}, {'case_id': b'dfd70c29-c72f-4cfe-9404-3ebb90334e19', 'evidence_id': b'1199505088', 'state': b'CHECKEDOUT', 'timestamp': 1713610310.321902}, {'case_id': b'dfd70c29-c72f-4cfe-9404-3ebb90334e19', 'evidence_id': b'1199505088', 'state': b'CHECKEDIN', 'timestamp': 1713610309.948364}, {'case_id': b'6fb433be-511c-4e88-9aa6-aed240ce7ea7', 'evidence_id': b'716953777', 'state': b'RELEASED', 'timestamp': 1713610309.198265}, {'case_id': b'6fb433be-511c-4e88-9aa6-aed240ce7ea7', 'evidence_id': b'716953777', 'state': b'CHECKEDIN', 'timestamp': 1713610309.198224}, {'case_id': b'dfd70c29-c72f-4cfe-9404-3ebb90334e19', 'evidence_id': b'1199505088', 'state': b'CHECKEDOUT', 'timestamp': 1713610308.45146}, {'case_id': b'dfd70c29-c72f-4cfe-9404-3ebb90334e19', 'evidence_id': b'1199505088', 'state': b'CHECKEDIN', 'timestamp': 1713610308.451403}, {'case_id': b'00000000-0000-0000-0000-000000000000', 'evidence_id': b'0', 'state': b'INITIAL', 'timestamp': 1713610308.080488}]

Test Failed: Never found timestamp field in log entry:
Case: 00000000-0000-0000-0000-000000000000
Item: 0
Action: INITIAL
Time: 1970-01-01T00:00:00Z
```

### Test #042 - log with random n > chain length (0/2)

```
Running command: `./bchoc init`
stdout from your program:
> Blockchain file not found. Created INITIAL block.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c 6d20922e-7861-4816-adff-3111974720a4 -i 2713342338 -g 4mg2TyrfHwCf -p C67C`
stdout from your program:
> Added item: 2713342338
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:24.127191Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc remove -i 2713342338 --why DISPOSED -p C67C`
stdout from your program:
> Item ID 2713342338 removed from the blockchain.
> Reason: DISPOSED

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c 4be0b220-b22f-470e-9cb7-bfa7dacc60c4 -i 3430629160 -g ASnVaen6xd4M -p C67C`
stdout from your program:
> Added item: 3430629160
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:24.869200Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 3430629160 -p E69E`
stdout from your program:
> Case: 4be0b220-b22f-470e-9cb7-bfa7dacc60c4
> Checked out item: 3430629160
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:52:25.241231Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c aff403fc-224a-434a-ab00-e7ea1c54d8fd -i 2593710326 -g FHi5Kv9gTl5y -p C67C`
stdout from your program:
> Added item: 2593710326
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:25.612075Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 2593710326 -p E69E`
stdout from your program:
> Case: aff403fc-224a-434a-ab00-e7ea1c54d8fd
> Checked out item: 2593710326
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:52:25.984281Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c 56407adc-f594-4e42-b63e-4423dfddc2cb -i 3939263117 -g z5hUmBiU0lYU -p C67C`
stdout from your program:
> Added item: 3939263117
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:26.355602Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 3939263117 -p L76L`
stdout from your program:
> Case: 56407adc-f594-4e42-b63e-4423dfddc2cb
> Checked out item: 3939263117
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:52:26.728199Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkin -i 2593710326 -p P80P`
stdout from your program:
> Case: aff403fc-224a-434a-ab00-e7ea1c54d8fd
> Checked in item: 2593710326
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:27.102125Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 2593710326 -p E69E`
stdout from your program:
> Case: aff403fc-224a-434a-ab00-e7ea1c54d8fd
> Checked out item: 2593710326
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:52:27.474408Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkin -i 3939263117 -p E69E`
stdout from your program:
> Case: 56407adc-f594-4e42-b63e-4423dfddc2cb
> Checked in item: 3939263117
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:27.846126Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 3939263117 -p L76L`
stdout from your program:
> Case: 56407adc-f594-4e42-b63e-4423dfddc2cb
> Checked out item: 3939263117
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:52:28.256582Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc show history -n 18 -p A65A`
stdout from your program:

stderr from your program:
~ Traceback (most recent call last):
~   File "/autograder/source/./bchoc", line 70, in <module>
~     main()
~   File "/autograder/source/./bchoc", line 61, in main
~     command.show_history(args.case_id, args.item_id, args.num_entries, args.reverse, args.password)
~   File "/autograder/source/command.py", line 55, in show_history
~     show_block.show_history(case_id, item_id, num_entries, reverse, password)
~   File "/autograder/source/show_block.py", line 142, in show_history
~     blocks = blocks[:num_entries]
~ TypeError: slice indices must be integers or None or have an __index__ method

Exit code of your program: 1


Test Failed: 1 != 0 : Program should have exited with code 0 with a valid block file, but it exited with an error code.
```

### Test #041 - log with random n < chain length (0/2)

```
Running command: `./bchoc init`
stdout from your program:
> Blockchain file not found. Created INITIAL block.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c b7e3e9d5-7989-47c1-9b63-36495832fc4c -i 3130536405 -g K9gZdC3i7fn6 -p C67C`
stdout from your program:
> Added item: 3130536405
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:29.452899Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc remove -i 3130536405 --why DISPOSED -p C67C`
stdout from your program:
> Item ID 3130536405 removed from the blockchain.
> Reason: DISPOSED

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c ca3e5bff-29e3-45e1-a689-ecc4ac742485 -i 461892951 -g rOa9FvNqHrg1 -p C67C`
stdout from your program:
> Added item: 461892951
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:30.200962Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc remove -i 461892951 --why DESTROYED -p C67C`
stdout from your program:
> Item ID 461892951 removed from the blockchain.
> Reason: DESTROYED

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c 66ac9147-b018-442b-9c3d-8449a17963a1 -i 2264878443 -g b0SHjXnCQWD9 -p C67C`
stdout from your program:
> Added item: 2264878443
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:30.941076Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 2264878443 -p P80P`
stdout from your program:
> Case: 66ac9147-b018-442b-9c3d-8449a17963a1
> Checked out item: 2264878443
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:52:31.309833Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c 72a2ce7f-c65e-4502-8f0d-694507777d8d -i 4240711007 -g XJowdhr9aT3g -p C67C`
stdout from your program:
> Added item: 4240711007
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:31.679597Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c ce161b7d-19e9-4495-b6b0-44b3a8ee61e1 -i 3097180969 -g HWeZTRtYN7LE -p C67C`
stdout from your program:
> Added item: 3097180969
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:32.048259Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc show history -n 5 -p L76L`
stdout from your program:

stderr from your program:
~ Traceback (most recent call last):
~   File "/autograder/source/./bchoc", line 70, in <module>
~     main()
~   File "/autograder/source/./bchoc", line 61, in main
~     command.show_history(args.case_id, args.item_id, args.num_entries, args.reverse, args.password)
~   File "/autograder/source/command.py", line 55, in show_history
~     show_block.show_history(case_id, item_id, num_entries, reverse, password)
~   File "/autograder/source/show_block.py", line 142, in show_history
~     blocks = blocks[:num_entries]
~ TypeError: slice indices must be integers or None or have an __index__ method

Exit code of your program: 1


Test Failed: 1 != 0 : Program should have exited with code 0 with a valid block file, but it exited with an error code.
```

### Test # - log without password (0/5)

```
Running command: `./bchoc init`
stdout from your program:
> Blockchain file not found. Created INITIAL block.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c b4df4aad-7908-41ca-b26d-b12976cdeef4 -i 503890620 -g xxLkRKiSUisx -p C67C`
stdout from your program:
> Added item: 503890620
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:33.162005Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc remove -i 503890620 --why RELEASED -p C67C`
stdout from your program:
> Item ID 503890620 removed from the blockchain.
> Reason: RELEASED

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c f479ee9d-dcf5-4bf1-bd4c-da0de594197f -i 418249476 -g iHkJjOBg99Bw -p C67C`
stdout from your program:
> Added item: 418249476
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:33.901012Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 418249476 -p L76L`
stdout from your program:
> Case: f479ee9d-dcf5-4bf1-bd4c-da0de594197f
> Checked out item: 418249476
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:52:34.273475Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkin -i 418249476 -p L76L`
stdout from your program:
> Case: f479ee9d-dcf5-4bf1-bd4c-da0de594197f
> Checked in item: 418249476
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:34.645194Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 418249476 -p P80P`
stdout from your program:
> Case: f479ee9d-dcf5-4bf1-bd4c-da0de594197f
> Checked out item: 418249476
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:52:35.019226Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c 75f59ce9-085f-493a-9d5f-b4582f8e8684 -i 1520445810 -g EmIL9M6rQFV7 -p C67C`
stdout from your program:
> Added item: 1520445810
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:35.394355Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc show history -i 503890620`
stdout from your program:

stderr from your program:
~ usage: bchoc show history [-h] [-c CASE_ID] [-i ITEM_ID] [-n NUM_ENTRIES] [-r]
~                           -p PASSWORD
~ bchoc show history: error: the following arguments are required: -p/--password

Exit code of your program: 2


Test Failed: 2 != 0 : Program should have exited with code 0 with a valid block file, but it exited with an error code.
```

### Test #025 - remove after checkin (destroyed) (0/2)

```
Running command: `./bchoc init`
stdout from your program:
> Blockchain file not found. Created INITIAL block.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c f3a5be29-faf7-4425-a4cd-fe280ff98b8a -i 2925919872 -g 2SzwiM7fzuQb -p C67C`
stdout from your program:
> Added item: 2925919872
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:44.296824Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 2925919872 -p L76L`
stdout from your program:
> Case: f3a5be29-faf7-4425-a4cd-fe280ff98b8a
> Checked out item: 2925919872
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:52:44.670154Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkin -i 2925919872 -p E69E`
stdout from your program:
> Case: f3a5be29-faf7-4425-a4cd-fe280ff98b8a
> Checked in item: 2925919872
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:45.041947Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc remove -i 2925919872 -y DESTROYED -p C67C`
stdout from your program:
> Item ID 2925919872 removed from the blockchain.
> Reason: DESTROYED

stderr from your program:

Exit code of your program: 0


Test Failed: False is not true : Block 4 in the chain doesn't equal the expected values (checksum and timestamp aren't checked). Check how you're storing the block.
Expected block values: Block(prev_hash=0, timestamp=1713610365.435896, case_id=b'90b5322d1af83097745a0fe3260d9f11', evidence_id=b'6cb95fa83f3d8807c481c556af7230c1', state=b'DESTROYED\x00\x00', creator=b'2SzwiM7fzuQb', owner=b'EXECUTIVE\x00\x00\x00', d_length=0, data=b'')
Values from your chain: Block(prev_hash=67429198042602037008172206844406468497801237947248303668377128722461120007437, timestamp=1713610365.414914, case_id=b'90b5322d1af83097745a0fe3260d9f11', evidence_id=b'42b7947879cc2d469b4c5c6024bfab35', state=b'DESTROYED\x00\x00\x00', creator=b'N\x00\x00\x002SzwiM7f', owner=b'zuQb\x00\x00\x00\x00\x00\x00\x00\x00', d_length=0, data=b'')
```

### Test #024 - remove after checkin (disposed) (0/2)

```
Running command: `./bchoc init`
stdout from your program:
> Blockchain file not found. Created INITIAL block.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c 744ab263-d93a-458c-8ebb-2426547ae4f0 -i 2579394023 -g OoCFi6wwbGuQ -p C67C`
stdout from your program:
> Added item: 2579394023
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:46.157275Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 2579394023 -p E69E`
stdout from your program:
> Case: 744ab263-d93a-458c-8ebb-2426547ae4f0
> Checked out item: 2579394023
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:52:46.527306Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkin -i 2579394023 -p L76L`
stdout from your program:
> Case: 744ab263-d93a-458c-8ebb-2426547ae4f0
> Checked in item: 2579394023
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:46.898679Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc remove -i 2579394023 -y DISPOSED -p C67C`
stdout from your program:
> Item ID 2579394023 removed from the blockchain.
> Reason: DISPOSED

stderr from your program:

Exit code of your program: 0


Test Failed: False is not true : Block 4 in the chain doesn't equal the expected values (checksum and timestamp aren't checked). Check how you're storing the block.
Expected block values: Block(prev_hash=0, timestamp=1713610367.28836, case_id=b'3ea7c51962be45beb9aed51ecedc28b0', evidence_id=b'ec4a2ce826ba11c892c8c4e975612c89', state=b'DISPOSED\x00\x00\x00', creator=b'OoCFi6wwbGuQ', owner=b'LAWYER\x00\x00\x00\x00\x00\x00', d_length=0, data=b'')
Values from your chain: Block(prev_hash=46927648996396270419885022126121879849871279477663213043255145489586112465778, timestamp=1713610367.267465, case_id=b'3ea7c51962be45beb9aed51ecedc28b0', evidence_id=b'4b857d12cf8b09861c7146650ca44007', state=b'DISPOSED\x00\x00\x00\x00', creator=b'N\x00\x00\x00OoCFi6ww', owner=b'bGuQ\x00\x00\x00\x00\x00\x00\x00\x00', d_length=0, data=b'')
```

### Test #026 - remove after checkin (released) (0/2)

```
Running command: `./bchoc init`
stdout from your program:
> Blockchain file not found. Created INITIAL block.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc add -c 51663f74-90f3-41b4-bd47-b9f5c471b052 -i 301966834 -g hTQcWYa0I4PY -p C67C`
stdout from your program:
> Added item: 301966834
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:48.012263Z
> Item(s) added successfully to the blockchain.

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkout -i 301966834 -p A65A`
stdout from your program:
> Case: 51663f74-90f3-41b4-bd47-b9f5c471b052
> Checked out item: 301966834
> Status: CHECKEDOUT
> Time of action: 2024-04-20T10:52:48.383115Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc checkin -i 301966834 -p P80P`
stdout from your program:
> Case: 51663f74-90f3-41b4-bd47-b9f5c471b052
> Checked in item: 301966834
> Status: CHECKEDIN
> Time of action: 2024-04-20T10:52:48.752825Z

stderr from your program:

Exit code of your program: 0

Running command: `./bchoc remove -i 301966834 -y RELEASED -p C67C`
stdout from your program:
> Item ID 301966834 removed from the blockchain.
> Reason: RELEASED

stderr from your program:

Exit code of your program: 0


Test Failed: False is not true : Block 4 in the chain doesn't equal the expected values (checksum and timestamp aren't checked). Check how you're storing the block.
Expected block values: Block(prev_hash=0, timestamp=1713610369.152425, case_id=b'3dd601124f3e5813aa33cb75bc0a9396', evidence_id=b'5d62d881137e534be56509f6c0171e38', state=b'RELEASED\x00\x00\x00', creator=b'hTQcWYa0I4PY', owner=b'POLICE\x00\x00\x00\x00\x00\x00', d_length=0, data=b'')
Values from your chain: Block(prev_hash=27442547132382153290433642657931609155097697008122190742008532594538459682411, timestamp=1713610369.130954, case_id=b'3dd601124f3e5813aa33cb75bc0a9396', evidence_id=b'563af6947c8aa32bf42978cdab08c0ae', state=b'RELEASED\x00\x00\x00\x00', creator=b'N\x00\x00\x00hTQcWYa0', owner=b'I4PY\x00\x00\x00\x00\x00\x00\x00\x00', d_length=0, data=b'')
```

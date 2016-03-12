/ $Id$
/ author:  Chao Zhu
/ descrip: Various tools to assist with the analysis of taq data.
/ prints a logline
/ msg_: type string
.taq.logline: {[msg_]
  0N!(string .z.Z), "   taq |  ", msg_;
  };
/ returns bool. path_ is a string, e.g. "/home/user"
.taq.path_exists: {[path_]
  not () ~ key hsym "S"$ path_
  };
/ returns a bool. file_ is a string, e.g. "my_file.csv".
/   file_ is either in the current path or must be fully qualified:
/     "/home/user/data/my_file.csv"
.taq.file_exists: {[file_]
  not () ~ key hsym "S"$ file_
  };
/ import a taq trade csv file into kdb. 
/ file_: type string.
.taq.import_trade_file: {[file_]

  if [not .taq.file_exists[file_];
    .taq.logline["file ", file_, " not found"];
    :()
  ];
  /generate a table named trade
  `trade set
    ("DTSFI"; enlist ",") 0: hsym "S"$ file_;

  .taq.logline["loaded file ", file_];
  .taq.logline["  there are ", (string count trade), " records"];
  };

/file1 is the input file
/file2 is the output file
/read input file and get output file
.taq.get_daily_vwap_file: {[file1_;file2_]
  .taq.import_trade_file[file1_];
  /calculate vwap by date and symbol
  temp :select vwap:(sum PRICE*VOLUME)%(sum VOLUME) by SYMBOL,DATE from trade;
  /`:(hsym "S"$ file2_) 0:.h.tx[`csv; temp];
  /save data to a csv
  (hsym "S"$ file2_) 0: .h.cd temp;
  };



<template>
  <div>
    <el-container v-loading="isLoading" element-loading-text="处理中"
    >
      <el-header>
        <NavBar></NavBar>
      </el-header>
      <el-main>
        <template v-if="hasPic">
          <PicShow :rawFilePath="dialogPath" :newFilePath="dialogNewPath" ></PicShow>
        </template>
        <template v-else>
          <div class="uploadpanel">
            <el-upload
              ref="upload"
              action="#"
              list-type="picture-card"
              :auto-upload="false"
              :on-change="handleChange"
            >
              <i slot="default" class="el-icon-plus"></i>
              <div slot="file" slot-scope="{file}">
                <img class="el-upload-list__item-thumbnail" :src="file.url" alt />
                <span class="el-upload-list__item-actions">
                  <span
                    class="el-upload-list__item-preview"
                    @click="handlePictureCardPreview(file)"
                  >
                    <i class="el-icon-zoom-in"></i>
                  </span>
                  <span
                    v-if="!disabled"
                    class="el-upload-list__item-delete"
                    @click="handleDownload(file)"
                  >
                    <i class="el-icon-download"></i>
                  </span>
                  <span
                    v-if="!disabled"
                    class="el-upload-list__item-delete"
                    @click="handleRemove(file)"
                  >
                    <i class="el-icon-delete"></i>
                  </span>
                </span>
              </div>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt />
            </el-dialog>
          </div>
          <el-button
            style="margin-left: 10px;margin-top:20px"
            size="small"
            type="success"
            @click="submitUpload"
          >开始去雾</el-button>

          <div class="settings">
            <Settings></Settings>
          </div>
        </template>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import NavBar from "./NavBar";
import PicShow from "./PicShow";
import Settings from "./Settings";

export default {
  name: "MainPanel",
  components: {
    NavBar,
    PicShow,
    Settings
  },
  data: function() {
    return {
      hasPic: false,
      isLoading: false,
      dialogImageUrl: "",
      dialogFile: null,
      dialogPath: "",
      dialogNewPath:"",
      dialogVisible: false,
      disabled: false
    };
  },
  methods: {
    submitUpload() {
      let request = require("request");
      let fs = require("fs");
      let path = require("path");
      const {app}  = require('electron').remote;
      let exePath = path.dirname(app.getPath('exe'));
      let exec = require("child_process").exec;

      let filePath = exePath+"\\..\\..\\..\\src\\renderer\\assets\\script\\dehaze.py";
      let inputFilePath=this.dialogPath;
      let inputFileName=inputFilePath.substr(inputFilePath.lastIndexOf('\\')+1);

      let outFileName="out_"+inputFileName
      let outputPath=inputFilePath.substr(0,inputFilePath.lastIndexOf('\\')+1);
      let thisInst=this;
      this.dialogNewPath=outputPath+outFileName;
      if (this.dialogImageUrl) {
        thisInst.isLoading=true;
        exec("python" + " " + filePath + " -i " + this.dialogPath+" -o "+outputPath+outFileName, function(
          err,
          stdout,
          stderr
        ) {
          if (err) {
            thisInst.isLoading=false;
            console.log("stderr", err);
          }
          if (stdout) {
            thisInst.isLoading=false;
            thisInst.hasPic = true;
            console.log("stdout", stdout);
          }
        });
      }
    },
    handleChange(file, fileList) {
      this.dialogFile = file;
      this.dialogImageUrl = file.url;
      this.dialogPath = file.raw.path;
    },
    handleRemove(file) {
      // console.log(file);
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    handleDownload(file) {
      // console.log(file);
    }
  }
};
</script>

<style scoped>
.el-header {
  padding: 0px !important;
}

.uploadpanel {
  margin-top: 20%;
}

.upload {
  margin-top: 0px;
}

.settings {
  position: absolute;
  top: 300px;
  right: 50px;
  width: 160px;
  border-width: 0px;
  border-style: solid;
  box-shadow: 1px 1px 1px 1px #f2f2f2;
}
</style>
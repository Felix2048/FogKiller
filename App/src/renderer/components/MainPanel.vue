<template>
    <div>
        <el-container>
            <el-header>
                <NavBar></NavBar>
            </el-header>
            <el-main>
                <template v-if="hasPic">
                    <PicShow :rawFilePath="dialogPath"></PicShow>
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
                            <img
                                class="el-upload-list__item-thumbnail"
                                :src="file.url" alt=""
                            >
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
                            <img width="100%" :src="dialogImageUrl" alt="">
                        </el-dialog>
                    </div>
                    <el-button style="margin-left: 10px;margin-top:20px" size="small" type="success" @click="submitUpload">开始去雾</el-button>
                  
                    <div class="settings">
                    <Settings></Settings>
                    </div>

                </template>
            </el-main>
        </el-container>
    </div>
</template>

<script>
import NavBar from './NavBar'
import PicShow from './PicShow'
import Settings from './Settings'

export default {
  name: 'MainPanel',
  components: {
    NavBar,
    PicShow,
    Settings
  },
  data: function () {
    return {
      hasPic: false,
      isLoading: false,
      dialogImageUrl: '',
      dialogFile:null,
      dialogPath:'',
      dialogVisible: false,
      disabled: false
    }
  },
  methods: {
    submitUpload () {
      let request = require('request');
      let fs = require('fs');
      let path = require('path');
      if(this.dialogImageUrl){
        console.log(this.dialogPath);
      }
      this.hasPic = true;
    },
    handleChange(file,fileList){
      this.dialogFile=file;
      this.dialogImageUrl=file.url;
      this.dialogPath=file.raw.path;
    },
    handleRemove (file) {
      // console.log(file);
    },
    handlePictureCardPreview (file) {
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    },
    handleDownload (file) {
      // console.log(file);
    }
  }
}
</script>

<style scoped>
.el-header{
    padding:0px !important
}

.uploadpanel{
    margin-top:20%
}

.upload{
    margin-top:0px;
}

.settings{
  position:absolute;
  top:300px;
  right:50px;
  width: 160px;
  border-width: 0px;
  border-style: solid;
  box-shadow: 1px 1px 1px 1px #f2f2f2;
}
</style>
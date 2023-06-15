import logging
from aiogram import Bot, Dispatcher, types, executor
import yt_dlp
import os
import time

bot = Bot(token='6291568207:AAENUfTsZPlOlaAD0rmxXmSyhpWPkbAek5M')
dp = Dispatcher(bot)

class FilenameCollectorPP(yt_dlp.postprocessor.common.PostProcessor):
    def init(self):
        super(FilenameCollectorPP, self).init(None)
        self.filenames = []

    def run(self, information):
        self.filenames.append(information["filepath"])
        return [], information

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.reply('Привет')

@dp.message_handler(commands=['cmd'])
async def search_cmd(message: types.Message):
    arg = message.get_args()
    YDL_OPTIONS = {
        'format': 'bestaudio/best',
        'noplaylist': 'True',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }
    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            ydl.extract_info(arg, download=False)
        except:
            filename_collector = FilenameCollectorPP()
            ydl.add_post_processor(filename_collector)
            video = ydl.extract_info(f'ytsearch:{arg}', download=True)['entries'][0]
            await message.reply_document(open(filename_collector.filenames[0], 'rb'))
            time.sleep(5)
            os.remove(filename_collector.filenames[0])
        else:
            video = ydl.extract_info(arg, download=True)
            await message.answer(f'Файл сохранен: {filename_collector.filenames[0]}')

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)